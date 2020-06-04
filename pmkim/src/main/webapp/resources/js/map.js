// ------------------------------------------------------------------------------ //
//
// Template name : kakaoMap - handler
// Categorie : map site page
// Author : oliver.yoo
// Version : v.1.0.0
// Created : 2020-06-04
// Last update : 2020-06-04
//
// ------------------------------------------------------------------------------ //


// 카카오 맵에서 넘어 오는 편의점명 -> CU, GS25, 세븐일레븐, 이마트24, 미니스톱
const EMART24 = "EM", CU = "CU", GS25 = "GS", SEVENELEVEN = "SE", MINISTOP = "MS";
var keyword = '<%=keyword%>';
var productName = '<%=keywordProduct%>';
var shop_code = '${vo.shop_code}';
var lat, lon;
var map; // 지도를 보여줄 변수
var geocoder; // 주소-좌표 변환 객체를 받을 변수
var infowindow;
var ps; // 장소 검색 객체를 받을 변수

var sumProductName = new Array();
var printGoodName = [], printEventName = [], printLength = 0;
var storeName = [], printProduct = [];
var mapContainer;
var markerImage;

// console.log("keyword: "+keyword);
// console.log("shop_code: "+shop_code);

// 검색어에 내위치, 내 위치, 공백을 검색하면 keyword가 편의점이 되고 내 위치 기반으로 편의점을
// 검색한다.
if(!isEmpty(keyword)){
	if(keyword == "내위치" || keyword == "내 위치"){
		keyword = '편의점';
	}else{
		if(isEmpty(shop_code)){
			console.log('what happen? shop_code error');
		}else{
			if(shop_code == 'ALL'){
				keyword += ' 편의점';
			}else if(shop_code == EMART24){
				keyword += ' 이마트24';
			}else if(shop_code == CU){
				keyword += ' CU';
			}else if(shop_code == GS25){
				keyword += ' GS25';
			}else if(shop_code == SEVENELEVEN){
				keyword += ' 세븐일레븐';
			}else if(shop_code == MINISTOP){
				keyword += ' 미니스톱';
			}else{
				console.log('편의점 검색 에러');
			}
		}
	}
	
}else{
	keyword = '편의점';
}

// 마커를 클릭하면 장소명을 표출할 인포윈도우 입니다
// 키워드 장소 검색할 때 필요한 부분!!
infowindow = new kakao.maps.InfoWindow({zIndex:1});
// 지도를 표시할 div
mapContainer = document.getElementById('map');

mapOption = { 
    center: new kakao.maps.LatLng(33.450701, 126.570667), // 지도의
															// 중심좌표
    level: 4 // 지도의 확대 레벨
};
// 지도를 생성합니다
map = new kakao.maps.Map(mapContainer, mapOption); 
// 주소-좌표 변환 객체를 생성합니다
geocoder = new kakao.maps.services.Geocoder();
// 장소 검색 객체를 생성합니다
ps = new kakao.maps.services.Places();
// -----------------------------------------------sssss----------------------------------------------------------
// HTML5의 geolocation으로 사용할 수 있는지 확인합니다
if (navigator.geolocation) {
	// console.log("geolocation!!!!!!!!!!!!!!");
	// GeoLocation을 이용해서 접속 위치를 얻어옵니다
	navigator.geolocation.getCurrentPosition(function(position) {
		lat = position.coords.latitude, // 위도
		lon = position.coords.longitude; // 경도
		// console.log("lat1: "+lat);
		// console.log("lon1: "+lon);
		// var locPosition = new kakao.maps.LatLng(lat, lon), //
		// 마커가 표시될 위치를 geolocation으로 얻어온 좌표로 생성합니다
		// message = '<div style="padding:5px;">편의점 명을 정확히
		// 기재해주세요!</div>'; // 인포윈도우에 표시될 내용입니다
		// 마커와 인포윈도우를 표시합니다
		// oneDisplayMarker(locPosition, message);

		ps.keywordSearch(keyword, placesSearchCB, {
			// LatLng : 중심 좌표. 특정 지역을 기준으로 검색한다.
			location: new kakao.maps.LatLng(lat, lon)
		});
	});
} else { // HTML5의 GeoLocation을 사용할 수 없을때 마커 표시 위치와 인포윈도우 내용을
			// 설정합니다
	var locPosition = new kakao.maps.LatLng(33.450701, 126.570667),
		message = '현재 위치를 찾을 수 없어요..'
		
	oneDisplayMarker(locPosition, message);

	ps.keywordSearch(keyword, placesSearchCB, {
		// LatLng : 중심 좌표. 특정 지역을 기준으로 검색한다.
		location: new kakao.maps.LatLng(lat, lon)
	});
}

// kakao 메서드 start------------------------
// 지도에 마커와 인포윈도우를 표시하는 함수입니다
function oneDisplayMarker(locPosition, message) {
    // locPosition 다름
    // 마커를 생성합니다
    var marker = new kakao.maps.Marker({  
        map: map, 
        position: locPosition
    }); 
    
    var iwContent = message, // 인포윈도우에 표시할 내용
        iwRemoveable = true;

    // 인포윈도우를 생성합니다
    // var infowindow = new kakao.maps.InfoWindow({
	infowindow = new kakao.maps.InfoWindow({
        content : iwContent,
        removable : iwRemoveable
    });
    
    // 인포윈도우를 마커위에 표시합니다
    infowindow.open(map, marker);
    
    // 지도 중심좌표를 접속위치로 변경합니다
    map.setCenter(locPosition);      
}

// 키워드 검색 완료 시 호출되는 콜백함수 입니다
function placesSearchCB (data, status, pagination) {
	// console.log(data[0].lat);
    if (status === kakao.maps.services.Status.OK) {
        // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
        // LatLngBounds 객체에 좌표를 추가합니다
        var bounds = new kakao.maps.LatLngBounds();

        for (var i=0; i<data.length; i++) {
			var str = data[i].place_name;
			
			// 클릭시 상품명과 이벤트명 이용!
			storeName[i] = str;

			// 추가!!
			var res = str.split(" ");
			// ex) cu, gs25 등..
			var shop_code = res[0];
			if(shop_code == '이마트24') shop_code = EMART24;
			else if(shop_code == 'GS25') shop_code = GS25;
			else if(shop_code == '세븐일레븐') shop_code = SEVENELEVEN;
			else if(shop_code == '미니스톱') shop_code = MINISTOP;
			else if(shop_code == 'CU') shop_code = CU;
			// ex) 테헤란로점, 종로1가점 등..
			var shop_name_detail = res[1];

			// map algorithm start
			if(isEmpty(productName)){
			}else{
				$.ajax({
					url:"/pmkim/map",
					type:'post',
					data: {
							"shop_code":shop_code,
							"shop_name_detail":shop_name_detail},
					dataType: "text",
					async: false,
					success:function(data){
						if(data == "success"){											
							// success면 카카오 맵에서 나온 편의점이 있다 라는것!!
							// 이제 부터는 이 편의점에 해당 상품이 행사하는지를 확인해서
							// 마커로 맵에 알려주면 끄~읏!
							var event_name = null, good_name = null;
							var resultName = getEventName(shop_code, productName);

							$.each(resultName, function(idx, val) {
								if(good_name == null) good_name = val.good_name + " ";
								if(event_name == null) event_name = val.event_name + " ";

								if(val.good_name != null) good_name += val.good_name + " ";
								if(val.event_name != null) event_name += val.event_name + " ";
							});
							
							if(isEmpty(good_name) || isEmpty(event_name)){
							}else{
								var resGoodName = good_name.split(" ");
								var resEventName = event_name.split(" ");
								
								printProduct[i] = new Array(resGoodName.length);
								for(var j = 0; j < resGoodName.length; j++){
									// 모든 상품들을 여기서 출력할수 있음
									if(!isEmpty(resGoodName[j]) || !isEmpty(resEventName[j])){
										// printProduct[i][j] =
										// removeDuplicatesArray(resGoodName[j]
										// + ": " +
										// resEventName[j]);
										printProduct[i][j] = resGoodName[j] + ": " + resEventName[j];
									}
									
								}
								// 출력용 변수
								printLength = resGoodName.length;
								printGoodName = resGoodName;
								printEventName = resEventName;

								// 대표적으로 처음에 나오는 상품 기준으로 지도에
								// 보여주기로함!!
								good_name = resGoodName[0];
								event_name = resEventName[0];
							}
							markerImage = null; // 행사 상품만 새로운
												// Image를 마커로
												// 나타내기 위해!!
							var imageSrc = null;
							if(isEmpty(event_name) || isEmpty(good_name)){
								console.log("nothing event_name or good_name");							
							}else{
								 // 마커의 이미지 주소입니다.
								if(event_name == '1+1' && shop_code == SEVENELEVEN){
									imageSrc = '/pmkim/resources/images/map/7eleven_1+1.png';
								}else if(event_name == '2+1' && shop_code == SEVENELEVEN){
									imageSrc = '/pmkim/resources/images/map/7eleven_2+1.png';
								}else if(event_name == '1+1' && shop_code == CU){
									imageSrc = '/pmkim/resources/images/map/cu_1+1.png';
								}else if(event_name == '2+1' && shop_code == CU){
									imageSrc = '/pmkim/resources/images/map/cu_2+1.png';
								}else if(event_name == '1+1' && shop_code == EMART24){
									imageSrc = '/pmkim/resources/images/map/emart24_1+1.png';
								}else if(event_name == '2+1' && shop_code == EMART24){
									imageSrc = '/pmkim/resources/images/map/emart24_2+1.png';
								}else if(event_name == '1+1' && shop_code == GS25){
									imageSrc = '/pmkim/resources/images/map/GS25_1+1.png';
								}else if(event_name == '2+1' && shop_code == GS25){
									imageSrc = '/pmkim/resources/images/map/GS25_2+1.png';
								}else if(event_name == '1+1' && shop_code == MINISTOP){
									imageSrc = '/pmkim/resources/images/map/ministop_1+1.png';
								}else if(event_name == '2+1' && shop_code == MINISTOP){
									imageSrc = '/pmkim/resources/images/map/ministop_2+1.png';
								}
								// 마커이미지의 크기입니다
								imageSize = new kakao.maps.Size(64, 69),
								// 마커이미지의 옵션입니다. 마커의 좌표와 일치시킬
								// 이미지 안에서의 좌표를 설정합니다.
								imageOption = {offset: new kakao.maps.Point(27, 69)}; 
								// 마커의 이미지정보를 가지고 있는 마커이미지를
								// 생성합니다
								markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imageOption)
							}
						
						}else{
							console.log("fail");
						}
					},
					error:function(jqXHR, textStatus, errorThrown){ //
						console.log("에러 발생!! \n textStatus: " + textStatus + " errorThrown: " + errorThrown + " jqXHR: "  + jqXHR);
					}
		    	});
			}
			
            searchDisplayMarker(data[i]);
			var location = new kakao.maps.LatLng(data[i].y, data[i].x); 
            bounds.extend(location);
        }       
		// -------------//-------------//-------------//-------------//-------------//-------------
        // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
        map.setBounds(bounds);
    } 
}

// 지도에 마커를 표시하는 함수입니다
function searchDisplayMarker(place) {
    // new kakao.maps.LatLng(place.y, place.x) 다름
    // 마커를 생성하고 지도에 표시합니다
	var marker = new kakao.maps.Marker({
			map: map,
			position: new kakao.maps.LatLng(place.y, place.x),
			image: markerImage // // 마커이미지 설정
    	});
	
	// 마커에 클릭이벤트를 등록합니다
    kakao.maps.event.addListener(marker, 'click', function() {
        // 마커를 클릭하면 장소명이 인포윈도우에 표출됩니다
        infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>');
        
        // console.log("test"+place.place_name);
		// printLength
		document.getElementById('printName').innerHTML = "";
		var idx = storeName.indexOf(place.place_name);
		
		// 상품 정보 보여주기
		try {
			// throw "myException"; // generates an exception
			for(var i = 0; i < printLength; i++){
				// console.log("loggggg("+i+"): "+
				// printProduct[idx][i]);
				if(i == printLength - 1){
					if(!isEmpty(printProduct[idx][i])){
						document.getElementById('printName').innerHTML += printProduct[idx][i];
					}
				}else{
					if(!isEmpty(printProduct[idx][i])){
						document.getElementById('printName').innerHTML += printProduct[idx][i] + ", ";
					}
				}

				// var id = "ctl03_Tabs1";
				// var lastFive = id.substr(id.length - 5); //
				// => "Tabs1"
				// var lastChar = id.substr(id.length - 1); //
				// => "1"
			}
		}
		catch (e) {
			// statements to handle any exceptions
			// logMyErrors(e); // pass exception object to error
			// handler
			console.log("오류"+e);
		}
		
		var reName = document.getElementById('printName').innerHTML;
		var lastChar = reName.substr(reName.length - 2);
		var lastCharDel;
		if(lastChar == ', '){
			lastCharDel = reName.substr(0, reName.length - 2);
			document.getElementById('printName').innerHTML = lastCharDel;
			// console.log("del----"+lastCharDel);
		}else{
			document.getElementById('printName').innerHTML
		}

		// console.log("test"+place.place_name);
        infowindow.open(map, marker);
    });

}

// kakao 메서드 end------------------------
function getEventName(shop_code, good_name){
	var result;
	// console.log("getEventName shop_code : " + shop_code);
	// console.log("getEventName good_name : " + good_name);
	
	$.ajax({
		url:"/pmkim/map/data",
		type:'post',
		data: {
				"shop_code":shop_code,
				"good_name":good_name},
		dataType: "json",
		// contentType: "application/x-www-form-urlencoded;
		// charset=UTF-8",
		async: false,
		success:function(data){
			result = data;
			// var productName = new Set();
			// document.getElementById('productList').innerHTML
			// = "검색된 상품: "
			
			// var temp;
			$.each(data, function(idx, val) {
				// console.log(idx + " " + val.good_name);
				// console.log(idx + " " + val.event_name);
				// document.getElementById('productList').innerHTML
				// += "<p id='result_name'>"+ val.good_name +
				// "</p>";
				// if(temp == null) sumProductName =
				// val.good_name;
				
				if(sumProductName == null) sumProductName = val.good_name;
				else sumProductName.push(val.good_name.trim());
				
			});
			
			sumProductName = removeDuplicatesArray(sumProductName);
			sumProductName.forEach( v => {
					document.getElementById('productList').innerHTML += v + " ";
			});

			// sumProductName = Array.from(new
			// Set(sumProductName));
			var filterSet;
			filterSet = removeDuplicatesArray(sumProductName);
			
			// sumProductName = Array.from(new
			// Set(sumProductName));
			// removeDuplicatesArray(sumProductName);
			// sumProductName
			
			if(sumProductName != null){
				document.getElementById('productList').innerHTML = "검색된 상품명: ";
				filterSet.forEach( v => {
					document.getElementById('productList').innerHTML += v + " ";
				});
			}else{
				document.getElementById('productList').innerHTML = "";
			}

		},
		error:function(jqXHR, textStatus, errorThrown){ //
			console.log("function 에러 발생!! \n textStatus: " + textStatus + " errorThrown: " + errorThrown + " jqXHR: "  + jqXHR);
		}
	});
	return result;
}
function removeDuplicatesArray(arr) {
	var tempArr = [];
	for (var i = 0; i < arr.length; i++) {
		if (tempArr.length == 0) {
			tempArr.push(arr[i]);
		} else {
			var duplicatesFlag = true;
			for (var j = 0; j < tempArr.length; j++) {
				if (tempArr[j].toLowerCase() == arr[i].toLowerCase()) {
					duplicatesFlag = false;
					break;
				}
			}
			if (duplicatesFlag) {
				tempArr.push(arr[i].toLowerCase());
				// console.log("duplicated : " + arr[i]);
			}
		}
	}
	return tempArr;
}

function isEmpty(str){
	if(typeof str == "undefined" || str == null || str == "")
		return true;
	else
		return false ;
}
		