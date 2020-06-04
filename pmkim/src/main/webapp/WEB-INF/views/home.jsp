<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"
	import = "vo.GoodsEventShopMemberVO,java.util.List,java.util.ArrayList"
%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<!DOCTYPE html>
<html lang="en">
<!-- Basic -->

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <!-- Mobile Metas -->
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Site Metas -->
    <title>편마, 김편복 - Home</title>
    <meta name="keywords" content="">
    <meta name="description" content="">
    <meta name="author" content="">

    <!-- Site Icons -->
    <link rel="icon" href="/pmkim/resources/images/pmkim.png"  type="image/png" sizes="16X16">
    <!--  Fonts -->
	<link rel="stylesheet" href= '//cdn.rawgit.com/young-ha/webfont-archive/master/css/Youth.css' type='text/css'>

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="/pmkim/resources/css/bootstrap.min.css">
    <!-- Site CSS -->
    <link rel="stylesheet" href="/pmkim/resources/css/style.css">
	<link rel="stylesheet" href="/pmkim/resources/css/style_home.css">
    <link rel="stylesheet" href="/pmkim/resources/css/style_nav.css">
    <link rel="stylesheet" href="/pmkim/resources/css/footerus.css">
    <!-- Responsive CSS -->
    <link rel="stylesheet" href="/pmkim/resources/css/responsive.css">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="/pmkim/resources/css/custom.css">

    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
	<script type="text/javascript"
	src="//dapi.kakao.com/v2/maps/sdk.js?appkey=da9ee51fb08b7986257790a5d30ebc55&libraries=services,clusterer,drawing"></script>
</head>

<body>
<%   
		    List<GoodsEventShopMemberVO> onelist = (ArrayList<GoodsEventShopMemberVO>) request.getAttribute("onelist");
			List<GoodsEventShopMemberVO> twolist = (ArrayList<GoodsEventShopMemberVO>) request.getAttribute("twolist");
			List<GoodsEventShopMemberVO> pblist = (ArrayList<GoodsEventShopMemberVO>) request.getAttribute("pblist");
%>
	<c:set var="sessionMemberId" value="${ sessionScope.id }"/>
    <!-- Start Main Top -->
    <header class="main-header">
        <!-- Start Navigation -->
        <nav class="navbar navbar-expand-lg navbar-light bg-light navbar-default bootsnav">
            <div class="container">
                <!-- Start Header Navigation -->
                <div class="navbar-header">
                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbar-menu" aria-controls="navbars-rs-food" aria-expanded="false" aria-label="Toggle navigation">
                    <i class="fa fa-bars"></i>
                </button>
                    <a class="navbar-brand" href="/pmkim/home"><img src="/pmkim/resources/images/pmkim_Logo_1.jpg" class="logo" alt=""></a>
                </div>
                <!-- End Header Navigation -->

                <!-- Collect the nav links, forms, and other content for toggling -->
                <div class="collapse navbar-collapse" id="navbar-menu">
                    <ul class="nav navbar-nav ml-auto" data-in="fadeInDown" data-out="fadeOutUp">
                        <li class="nav-item active"><a class="nav-link" href="/pmkim/home">Home</a></li> <!-- href는 jsp/html 형식이 아닌, {/매핑명}으로  해주시면돼용! 나중에 고쳐주세요~ -->
                        <li class="nav-item active"><a class="nav-link" href="/pmkim/map">지도</a></li> <!--성진오빠파트-->
                        <li class="nav-item active"><a class="nav-link" href="/pmkim/analysis">SNS 분석</a></li> <!-- 세호-->
                        <li class="nav-item active"><a class="nav-link" href="/pmkim/event">행사</a></li> <!-- 지혜파트-->
                        <li class="nav-item active"><a class="nav-link" href="/pmkim/cart">만원의 행복</a></li> <!-- 규영언니파트♡ -->
                        <li class="nav-item active"><a class="nav-link" href="/pmkim/news">편의점 뉴스</a></li> <!-- 규영언니파트♡ -->
                        <!-- <li class="nav-item active"><a class="nav-link" data-toggle="modal" data-target="#loginModal" href="/pmkim/#">로그인</a></li>	                        
						<li class="nav-item active"><a class="nav-link" href="/pmkim/signup">회원가입</a></li> -->
						<!-- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; -->
						<c:choose>
							<c:when test="${msg eq 'success' || !empty sessionMemberId}">
								<li class="nav-item active"><a class="nav-link" id="userView" href="/pmkim/ownerpage"><img src="/pmkim/resources/images/star.png" style="width:13px;">${sessionMemberId}님</a></li>
								<li class="nav-item active"><a class="nav-link" id="logout" href="/pmkim/logout"><b>Logout</b></a></li>
								
							</c:when>
							<c:when test="${msg eq 'fail' || msg eq 'logout' || msg eq '' || msg eq null}">
								<li class="nav-item active"><a class="nav-link" id="login" data-toggle="modal" data-target="#loginModal" href="/pmkim/#">로그인</a></li>
								<li class="nav-item active"><a class="nav-link" id="signup" href="/pmkim/signup">회원가입</a></li>	
						    </c:when>
						</c:choose>
                    </ul>
                </div>
                <!-- /.navbar-collapse -->
			
            </div>
            
        </nav>
        <!-- End Navigation -->
    </header>
    <!-- End Main Top -->
    
    <!-- Start login popup -->
    <div class="container">
		<!-- <button type="button" class="btn btn-info btn-round" data-toggle="modal" data-target="#loginModal">
		    Login
		</button>   -->
		<div class="modal fade" id="loginModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
			
		  <div class="modal-dialog modal-dialog-centered" role="document" >
		    <div class="modal-content" >
		      <div class="modal-header border-bottom-0">
		        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
		          <span aria-hidden="true">&times;</span>
		        </button>
		      </div>
		      <div class="modal-body border-bottom-0">
		      	<div class="form-title text-center"><!--  style="margin-left:auto; margin-right:auto;" -->
					<img src="/pmkim/resources/images/pmkim_Logo_1.jpg" /> 	
				</div>
				<br>
				
		        <div class="form-title text-center">
		          <h4><b>Login</b></h4>
		        </div>
		        <div class="d-flex flex-column text-center">
		        
		          <form method="post" action="/pmkim/login" id="frmSignin">
		            <div class="form-group">
		              <input type="text" class="form-control" name="id" placeholder="Your id...">
		            </div>
		            <div class="form-group">
		              <input type="password" class="form-control" name="pw" placeholder="Your password...">
		            </div>
		            <button type="submit" class="btn btn-info btn-block btn-round" id="btnLogin" style="background-color:#0F694D">Login</button> <!-- '/weet/signinCheck.do' -->
		          </form>
		          
		          <!-- <div class="text-center text-muted delimiter">or use a social network</div> -->
		          <div class="d-flex justify-content-center social-buttons">
		            <!-- <button type="button" id="btnGoogleSignin" class="btn btn-secondary btn-round" data-toggle="tooltip" data-placement="top" title="Google"
		           		onclick="
		           			gauth.signIn().then(function(){
								console.log('gauth.signIn()');
								checkLoginStatus();
								location.reload(true);
							});
						" data-dismiss="modal">
		          		<img src="/pmkim/resources/images/btn_google_light_normal_ios.svg">
		          	</button> -->
		          </div>
		        </div>
		      </div>
		      <div class="modal-footer d-flex justify-content-center ">
			        <div class="signup-section text-center">Not a member yet? 
			        	<a href="/pmkim/signup">Sign Up</a>.
			        </div>
			        <button type="button" class="btn btn-default text-center" data-dismiss="modal">Close</button>
			        <!-- <button type="button" class="btn btn-info btn-lg" data-toggle="modal" data-target="#signupModal">Open Modal</button> -->
		      </div>
		    </div>
		      
		  </div>
		</div>
		
	</div>
		<!-- End login popup -->
    
	<!-- Start Slider -->
    <div id="slides-shop" class="cover-slides">
        <ul class="slides-container">
            <li class="text-center">
                <img src="/pmkim/resources/images/home1.png" alt="">
                <div class="container">
                    <div class="row">
                        <div class="col-md-12">
                            <h1 class="header-words"><a href="/pmkim/event"> 행사상품 둘러보기 </a></h1>
                        </div>
                    </div>
                </div>
            </li>
            <li class="text-center">
                <img src="/pmkim/resources/images/home2.png" alt="">
                <div class="container">
                    <div class="row">
                        <div class="col-md-12">
                        </div>
                    </div>
                </div>
            </li>
            <li class="text-center">
                <img src="/pmkim/resources/images/home3.png" alt="">
                <div class="container">
                    <div class="row">
                        <div class="col-md-12">
                             <h1 class="header-words"><a href="/pmkim/cart"> 만원의 행복 내가 만들어보기 </a></h1>
                        </div>
                    </div>
                </div>
            </li>
        </ul>
        <div class="slides-navigation">
            <a href="#" class="next"><i class="fa fa-angle-right" aria-hidden="true"></i></a>
            <a href="#" class="prev"><i class="fa fa-angle-left" aria-hidden="true"></i></a>
        </div>
    </div>
    <!-- End Slider -->



	<!-- Start MAP  -->
    <div class="products-box33">
        <div class="container">
        	<br>
                <div class="col-lg-12">
                    <div class="title-all text-center">
                    <img class="map-img" src ="/pmkim/resources/images/gs.png"/>
                    <img class="map-img" src ="/pmkim/resources/images/cu1.png"/>
                    <img class="map-img" src ="/pmkim/resources/images/emart24.png"/>
                    <img class="map-img" src ="/pmkim/resources/images/ministop.png"/>
                    <img class="map-img-small" src ="/pmkim/resources/images/seveneleven.png"/><br><br>
                    <a class="event-href" href="/pmkim/map">지도</a><br>
                     <a class="event-a" href="/pmkim/map">주변의 편의점을</a>
                     <a class="event-a" href="/pmkim/map" style="color:red">찾아보세요~</a><br>
                     <a class="event-a" href="/pmkim/map" style="color:grey">이곳을 클릭해보세요!</a><br><br>
                    <div id="map" class="map-border" style="width: 100%; height: 500px;"></div>
                    </div>
                </div>
    	</div>
    </div>
    <!-- End MAP  -->




	<!-- Start Products  -->
    <div class="products-box">
        <div class="container">
 
			<div class="row">
                <div class="col-lg-12">
                    <div class="title-all text-center">
                        <a class="event-href" href="/pmkim/event">행사상품</a><br>
                        <a class="event-a" href="/pmkim/event">더 많은</a>
                         <a class="event-a" href="/pmkim/event" style="color:red">브랜드의 행사</a>
                         <a class="event-a" href="/pmkim/event">브랜드의 행사를 보기 위해서 이곳을 클릭해주세요!</a><br><br>
                        <a>
                        	<img class="event-img" src ="/pmkim/resources/images/gs.png"/>
                        	<img class="event-img" src ="/pmkim/resources/images/cu1.png"/>
                        	<img class="event-img" src ="/pmkim/resources/images/emart24.png"/>
                        	<img class="event-img" src ="/pmkim/resources/images/ministop.png"/>
                        	<img class="event-img-small" src ="/pmkim/resources/images/seveneleven.png"/>
                        </a>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-12">
                    <div class="special-menu text-center">
                        <div class="button-group filter-button-group">
                            <button class="active" data-filter="*">전체보기</button>
                            <button data-filter=".oneOne">1+1</button>
                            <button data-filter=".twoOne">2+1</button>
                        	<button data-filter=".pb">PB</button>
                        </div> 
                    </div>
                </div>
            </div>
			
			
			
            <div class="row special-list">
             <c:forEach var="vo2" items="${twolist}" begin="1" end="5">
                <div class="col-lg-3 col-md-6 special-grid twoOne">
                    <div class="products-single fix">
                        <div class="box-img-hover">
                            <div class="type-lb">
                                <p class="sale">${vo2.shop_name} ${vo2.event_name }</p>
                            </div>
                            <img src="${vo2.good_img}" style="height:280px;" class="img-fluid" alt="Image">
                        </div>
                        <div class="why-text">
                            <h3>${vo2.good_name}</h3> <!-- FROM GOODS -->
                            <h4>${vo2.mfg_name}</h4>
                            <h5>${vo2.good_price}원</h5> <!-- FROM GOODS -->
                        </div>
                    </div>
                </div>
             </c:forEach>
                
             <c:forEach var="vo1" items="${onelist}" begin="1" end="5">
                <div class="col-lg-3 col-md-6 special-grid oneOne">
                    <div class="products-single fix">
                   
                        <div class="box-img-hover">
                            <div class="type-lb">
                                <p class="sale">${vo1.shop_name} ${vo1.event_name }</p>
                            </div>
                            <img src="${vo1.good_img}" style="height:280px;"class="img-fluid" alt="Image">
                        </div>
                        <div class="why-text">
                            <h3>${vo1.good_name}</h3> <!-- FROM GOODS -->
                            <h4>${vo1.mfg_name}</h4>
                            <h5>${vo1.good_price}원</h5> <!-- FROM GOODS -->
                        </div>
                        
                    </div> 
                </div>
               </c:forEach>
               
               <c:forEach var="vo3" items="${pblist}" begin="1" end="5">
                <div class="col-lg-3 col-md-6 special-grid pb">
                    <div class="products-single fix">
                   
                        <div class="box-img-hover">
                            <div class="type-lb">
                                <p class="sale">${vo3.shop_name} ${vo3.event_name }</p>
                            </div>
                            <img src="${vo3.good_img}" style="height:280px;" class="img-fluid" alt="Image">
                        </div>
                        <div class="why-text">
                            <h3>${vo3.good_name}</h3> <!-- FROM GOODS -->
                            <h4>${vo3.mfg_name}</h4>
                            <h5>${vo3.good_price}원</h5> <!-- FROM GOODS -->
                        </div>
                        
                    </div> 
                </div>
               </c:forEach>
            </div>
        </div> 
    </div>
    <!-- End Products  -->
    
    
    <!-- Start Blog  -->
    <div class="latest-blog">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <div class="title-all text-center">
                   		 <a class="event-href" href="/pmkim/analysis">SNS분석</a><br>
                        <a class="event-a" href="/pmkim/analysis"></a>
                         <a class="event-a" href="/pmkim/analysis" style="color:red">인기 있는</a>
                         <a class="event-a" href="/pmkim/analysis">편의점 SNS 분석을 보기위해서 이곳을 클릭해주세요!</a><br><br>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-md-6 col-lg-4 col-xl-4">
                    <div class="blog-box">
                        <div class="blog-img">
                            <img class="img-fluid" src="/pmkim/resources/images/a_1.jpg" alt="" />
                        </div>
                        <div class="blog-content">
                            <div class="title-blog">
                                <h3>1위, 세븐일레븐</h3>
                                <p>편의점 7-Eleven, 가맹점주 모집 및 점포개발사업, 예약도시락, 멤버쉽, 택배 서비스 안내.</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 col-lg-4 col-xl-4">
                    <div class="blog-box">
                        <div class="blog-img">
                            <img class="img-fluid" src="/pmkim/resources/images/a_2.jpg" alt="" />
                        </div>
                        <div class="blog-content">
                            <div class="title-blog">
                                <h3>2위, GS25</h3>
                                <p>일상생활의 중심, 하루의 시작 Lifestyle Platform GS25</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 col-lg-4 col-xl-4">
                    <div class="blog-box">
                        <div class="blog-img">
                            <img class="img-fluid" src="/pmkim/resources/images/a_3.jpg" alt="" />
                        </div>
                        <div class="blog-content">
                            <div class="title-blog">
                                <h3>3위, CU</h3>
                                <p>편의점 미니스톱 소개, 소매점 개업 안내, 경영주 모집, 신상품 정보 및 고객정보.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- End Blog  -->

    
	<!-- Start Footer  -->
	<footer>
		<div class="footer-main">
			<div class="container3">
				<div class="row">
					<div class="col-lg-4 col-md-12 col-sm-12">
						<div class="footer-top-box">
							<h3>챗봇(Coming Soon)</h3>
						</div>
					</div>
				</div>
				<br><br>
				<div class="row">
					<div class="col-lg-4 col-md-12 col-sm-12">
						<div class="footer-top-box">
							<h3>We are One ; 곰돌이 감자 </h3>
						</div>
					</div>
				</div>

				<div class="container text-centers">
					<div class="row">
						<!-- Footer 1-->
						<div class="col-lg-422 mb-5 mb-lg-0">
							<a><img src="/pmkim/resources/images/haley.png" class="profile"  alt="" /></a><br><br>
							<a href="https://github.com/JihyeHaley" class="result-text">Haley Oh</a><br><br>
							<a class="result-text">You know? I'm 팀장4;)</a><br><br>
						<a class= "profile-text">has kinda professional language skills English, Chinese, Japanese. Currently working and studying for full-stack developing skills</a>
						
						</div>

						<!-- Footer 2-->
						<div class="col-lg-422 mb-5 mb-lg-0">
							<a><img src="/pmkim/resources/images/seho.png" class="profile"   alt="" /></a><br><br>
							<a href="https://github.com/sehooh5" class="result-text">Seho Oh </a><br><br>
							<a class="result-text">You know? I'm 팀장1;)</a><br><br>
							<a class= "profile-text">is one of the treasurous in gomgam since he has professional analysis skills based on R selenium. His main major was Design. Amazing!</a>
						
						</div>

						<!-- Footer 3-->
						<div class="col-lg-422 mb-5 mb-lg-0">
							<a><img src="/pmkim/resources/images/linda.png" class="profile" alt="" /></a><br><br>
							<a href="https://github.com/GyuyoungEom" class="result-text">Linda Eom </a><br><br>
							<a  class="result-text">You know? I'm 팀장3;)</a><br><br>
							<a class= "profile-text">without her, this work could not be achieved... haha He is superwomen among us. Her diction is based on Austrailia, and she is familiar at super power on everything..!!!! </a>
						</div>

						<!-- Footer 4-->
						<div class="col-lg-422 mb-5 mb-lg-0">
							<a><img src="/pmkim/resources/images/oliver.png" class="profile"  /></a><br><br>
							<a href="https://github.com/SeongjinOliver" class="result-text">Oliver Yoo </a><br><br>
							<a class="result-text">You know? I'm 팀장1;)</a><br><br>
							<a class= "profile-text">is amazing man because he is familiar with back-frond end, DB, Spring, and Java, C... Cannot count all LOL. Surprise thing is he is even studying himself at every night despite project season :)</a>
							
							
						</div>
					</div>
				</div>


				<div class="row">
					<div class="col-lg-4 col-md-12 col-sm-12">
						<div class="footer-widget" ">
							<h4>About 편마 김편복</h4>
							<p class="result-text">편의점 마스터! 김편복
								데이터, 위치기반을 활용한 편의점 상품 추천 서비스</p>
							<p class="result-text">편의점에서 점심을 간단히 먹고 싶은 김편복씨는 자신의 위치에서 먹고자하는
								상품 어느 편의점에서 행사를 하는지 알고 싶은데 알 수 있는 방법이 없다!!
								이럴때 필요한 서비스는 "<b>편마 김편복</b>"</p>
						</div>
					</div>
					<div class="col-lg-4 col-md-12 col-sm-12">
						<div class="footer-link result-text">
							<h4>Information</h4>
								<a href="#/pmkim/home" >  HOME</a><br>
								<a href="#/pmkim/map">  지도</a><br>
								<a href="#/pmkim/analysis">  SNS 분석</a><br>
								<a href="#/pmkim/event">  행사</a><br>
								<a href="#/pmkim/cart">  만원의 행복</a><br>
								<a href="#/pmkim/cart">  편의점 뉴스</a>
						</div>
					</div>
					<div class="col-lg-4 col-md-12 col-sm-12">
						<div class="footer-link-contact result-text">
							<h4>Contact Us</h4>
							<ul>
								<li>
									<p>
										<i class="fas fa-map-marker-alt"></i>주소: 서울특별시 강남구 
										테헤란로 212 <br>(역삼동 718-5번지)<br> (우) 06220
									</p>
								</li>
								<li>
									<p>
										<i class="fas fa-phone-square"></i>Phone: <a
											href="tel:+81-1029852154">+82-10 2985 2154</a>
									</p>
								</li>
								<li>
									<p>
										<i class="fas fa-envelope"></i>Email: <a
											href="mailto:ohhojh@gmail.com">ohhojh@gmail.com</a>
									</p>
								</li>
							</ul>
						</div>
					</div>
				</div>
			</div>
		</div>
	</footer>
	<!-- End Footer  -->
	<!-- Start copyright  -->
	<div class="footer-copyright">
		<p class="footer-company">
			All Rights Jihye Oh. &copy; 2020 <a href="#">PM, KIM</a> Design By GomGam
		</p>
	</div>
	<!-- End copyright  -->

    <a href="#" id="back-to-top" title="Back to top" style="display: none;">&uarr;</a>
    
    <!-- MAP -->
    <script>
		// 마커를 클릭하면 장소명을 표출할 인포윈도우 입니다
		var infowindow = new kakao.maps.InfoWindow({zIndex:1});
		
		var mapContainer = document.getElementById('map'), // 지도를 표시할 div 
		    mapOption = {
		        center: new kakao.maps.LatLng(37.566826, 126.9786567), // 지도의 중심좌표
		        level: 3 // 지도의 확대 레벨
		    };  
		
		// 지도를 생성합니다    
		var map = new kakao.maps.Map(mapContainer, mapOption); 
		
		// 장소 검색 객체를 생성합니다
		var ps = new kakao.maps.services.Places(); 
		
		// 키워드로 장소를 검색합니다
		//ps.keywordSearch('편의점', placesSearchCB);
		
		var imageSrc = null, 
    	imageSize = new kakao.maps.Size(64, 69), // 마커이미지의 크기입니다
	    imageOption = {offset: new kakao.maps.Point(27, 69)}; // 마커이미지의 옵션입니다. 마커의 좌표와 일치시킬 이미지 안에서의 좌표를 설정합니다.
	 	// 마커의 이미지정보를 가지고 있는 마커이미지를 생성합니다
	    var markerImage;
	    
		if (navigator.geolocation) {
			//console.log("geolocation!!!!!!!!!!!!!!");
			// GeoLocation을 이용해서 접속 위치를 얻어옵니다
			navigator.geolocation.getCurrentPosition(function(position) {
				lat = position.coords.latitude, // 위도
				lon = position.coords.longitude; // 경도
				//console.log("lat1: "+lat);
				//console.log("lon1: "+lon);
				// var locPosition = new kakao.maps.LatLng(lat, lon), // 마커가 표시될 위치를 geolocation으로 얻어온 좌표로 생성합니다
				//     message = '<div style="padding:5px;">편의점 명을 정확히 기재해주세요!</div>'; // 인포윈도우에 표시될 내용입니다
				//마커와 인포윈도우를 표시합니다   
				// oneDisplayMarker(locPosition, message);

				ps.keywordSearch('편의점', placesSearchCB, {
					// LatLng : 중심 좌표. 특정 지역을 기준으로 검색한다.
					location: new kakao.maps.LatLng(lat, lon)
				});
			});
		} else { // HTML5의 GeoLocation을 사용할 수 없을때 마커 표시 위치와 인포윈도우 내용을 설정합니다
			var locPosition = new kakao.maps.LatLng(33.450701, 126.570667),
				message = '현재 위치를 찾을 수 없어요..'
				
			oneDisplayMarker(locPosition, message);

			ps.keywordSearch('편의점', placesSearchCB, {
				// LatLng : 중심 좌표. 특정 지역을 기준으로 검색한다.
				location: new kakao.maps.LatLng(locPosition)
			});
		}
		
		// 키워드 검색 완료 시 호출되는 콜백함수 입니다
		function placesSearchCB (data, status, pagination) {
		    if (status === kakao.maps.services.Status.OK) {
		
		        // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
		        // LatLngBounds 객체에 좌표를 추가합니다
		        var bounds = new kakao.maps.LatLngBounds();
		
		        for (var i=0; i<data.length; i++) {
		        	var str = data[i].place_name;
		        	var res = str.split(" ");
		        	var shop_code = res[0];
		        	console.log("shop code  "+shop_code);
		        	
		        	// 마커이미지의 주소입니다
		        	if(shop_code == 'CU'){
		        		imageSrc = '/pmkim/resources/images/cu1.png';
		        	}else if(shop_code == 'GS25'){
		        		imageSrc = '/pmkim/resources/images/map/gs_home.png';
		        	}else if(shop_code == '이마트24'){
		        		imageSrc = '/pmkim/resources/images/map/e24.png';
		        	}else if(shop_code == '세븐일레븐'){
		        		imageSrc = '/pmkim/resources/images/seveneleven.png';
		        	}else if(shop_code == '미니스톱'){
		        		imageSrc = '/pmkim/resources/images/map/ministop_home.png';
		        	}else imageSrc = null;
		        	
		        	markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imageOption);
		        	//console.log("place name2 : "+data[i].place_name)
		            displayMarker(data[i]);
	
					var location = new kakao.maps.LatLng(data[i].y, data[i].x); 
                    bounds.extend(location);
		            //bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
		        }       
		
		        // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
		        map.setBounds(bounds);
		    } 
		}
		
		// 지도에 마커를 표시하는 함수입니다
		function displayMarker(place) {
		    
		    // 마커를 생성하고 지도에 표시합니다
		    var marker = new kakao.maps.Marker({
		        map: map,
		        image: markerImage,
		        position: new kakao.maps.LatLng(place.y, place.x) 
		    });

        	
		    // 마커에 클릭이벤트를 등록합니다
		    kakao.maps.event.addListener(marker, 'click', function() {
		        // 마커를 클릭하면 장소명이 인포윈도우에 표출됩니다
		        infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>');
		        infowindow.open(map, marker);
		    });
		}
	</script>
    
    <!-- END MAP -->

    <!-- ALL JS FILES -->
    <script src="/pmkim/resources/js/jquery-3.2.1.min.js"></script>
    <script src="/pmkim/resources/js/popper.min.js"></script>
    <script src="/pmkim/resources/js/bootstrap.min.js"></script>
    <!-- ALL PLUGINS -->
    <script src="/pmkim/resources/js/jquery.js_analysis.js"></script>
    <script src="/pmkim/resources/js/jquery.superslides.min.js"></script>
    <script src="/pmkim/resources/js/bootstrap-select.js"></script>
    <script src="/pmkim/resources/js/inewsticker.js"></script>
    <script src="/pmkim/resources/js/bootsnav.js"></script>
    <script src="/pmkim/resources/js/images-loded.min.js"></script>
    <script src="/pmkim/resources/js/isotope.min.js"></script>
    <script src="/pmkim/resources/js/owl.carousel.min.js"></script>
    <script src="/pmkim/resources/js/baguetteBox.min.js"></script>
    <script src="/pmkim/resources/js/form-validator.min.js"></script>
    <script src="/pmkim/resources/js/contact-form-script.js"></script>
    <script src="/pmkim/resources/js/custom.js"></script>
</body>

</html>
