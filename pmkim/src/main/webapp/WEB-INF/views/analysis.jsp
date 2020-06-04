<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
   pageEncoding="UTF-8"
   import="java.util.List, java.util.ArrayList,vo.AnalysisVO"%>
<%@page import="java.util.Base64"%>
<!DOCTYPE html>
<html lang="en">
<!-- Basic -->

<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">

<!-- Mobile Metas -->
<meta name="viewport" content="width=device-width, initial-scale=1">

<!-- Site Metas -->
<title>편마, 김편복 - SNS 분석</title>
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
<link rel="stylesheet" href="/pmkim/resources/css/style_analysis.css">
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

<script src="/pmkim/resources/js/htmlwidgets.js"></script>
<link href="/pmkim/resources/css/wordcloud.css" rel="stylesheet" />
<script src="/pmkim/resources/js/wordcloud2-all.js"></script>
<script src="/pmkim/resources/js/hover.js"></script>
<script src="/pmkim/resources/js/wordcloud2.js"></script>
<script src="/pmkim/resources/js/jquery-3.2.1.min.js"></script>
<script src="http://d3js.org/d3.v3.min.js" charset = "utf-8"></script>
<style>
#myGraph rect {
	stroke-width : 1px;
	fill : orange;
}
svg {
	width : 500px;
	height : 180px;
}
.text {
        font-weight: bold;
        color: #ffffff;
         text-shadow: 2px 2px 2px gray; 
}
</style>
</head>

<body>


   <!-- Start Main Top -->
   <c:set var="sessionMemberId" value="${ sessionScope.id }"/>
   <header class="main-header">
      <!-- Start Navigation -->
      <nav
         class="navbar navbar-expand-lg navbar-light bg-light navbar-default bootsnav">
         <div class="container">
            <!-- Start Header Navigation -->
            <div class="navbar-header">
               <button class="navbar-toggler" type="button" data-toggle="collapse"
                  data-target="#navbar-menu" aria-controls="navbars-rs-food"
                  aria-expanded="false" aria-label="Toggle navigation">
                  <i class="fa fa-bars"></i>
               </button>
               <a class="navbar-brand" href="/pmkim/home"><img
                  src="resources/images/pmkim_Logo_1.jpg" class="logo" alt=""></a>
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
    

   <!-- Start All Title Box -->
   <div class="all-title-box">
      <div class="container">
         <div class="row">
            <div class="col-lg-12">
               <h2>SNS ANALYSIS</h2>
            </div>
         </div>
      </div>
   </div>
   <!-- End All Title Box -->

   <!-- Start Shop Detail  -->
   <div class="shop-detail-box-main">
      <div class="container">
         <div class="row">
            <div class="col-xl-5 col-lg-5 col-md-6">
               <div id="carousel-example-1"
                  class="single-product-slider carousel slide" data-ride="carousel" data-interval="false">
                  <div class="carousel-inner" role="listbox">
                     <div class="carousel-item active" id="SE">
                     <input type="hidden" class="shop" id="SE">
                        <div class="type-lb">
                                <p class="sale">best 1</p>
                                 </div>
                        <a href ="/pmkim/analysis">
                        <img class="d-block w-100" src="/pmkim/resources/images/seveneleven.png"
                           alt="First slide"></a>
                     </div>
                     <div class="carousel-item" id="GS">
                     <input type="hidden" class="shop" id="GS">
                        <div class="type-lb">
                                <p class="sale">best 2</p>
                                 </div>
                        <img class="d-block w-100"
                           src="/pmkim/resources/images/gs25.png" alt="Second slide">
                     </div>
                     <div class="carousel-item" id="MS">
                     <input type="hidden" class="shop" id="MS">
                        <div class="type-lb">
                                <p class="sale">best 3</p>
                                 </div>
                        <img class="d-block w-100"
                           src="/pmkim/resources/images/mini.png" alt="Third slide">
                     </div>
                     <div class="carousel-item" id="EM">
                     <input type="hidden" class="shop" id="EM">
                        <div class="type-lb">
                                <p class="sale">best 4</p>
                                 </div>
                        <img class="d-block w-100"
                           src="/pmkim/resources/images/emart24.png" alt="Fourth slide">
                     </div>
                     <div class="carousel-item" id="CU" >
                     <input type="hidden" class="shop" id="CU">
                        <div class="type-lb">
                                <p class="sale">best 5</p>
                                 </div>
                        <img class="d-block w-100"
                           src="/pmkim/resources/images/cu.png" alt="Fifth slide">
                     </div>
                  </div>
                  <a class="carousel-control-prev" href="#carousel-example-1"
                     role="button" data-slide="prev" id="next-carousel"> <i class="fa fa-angle-left"
                     aria-hidden="true"></i> <span class="sr-only">Previous</span>
                  </a> 
                  <a class="carousel-control-next" href="#carousel-example-1"
                     role="button" data-slide="next" id="next-carousel"> <i class="fa fa-angle-right"
                     aria-hidden="true"></i> <span class="sr-only">Next</span>
                  </a>
               </div>
            </div>
            
            
<script>
				
			    	function wordcloud(shop_code){
						var url = "/pmkim/resources/html/"+shop_code+".html";
						$.ajax({
							  url:url,
							  context: document.body,
							  success: function(response){
								//console.log(url);
							    html = response;
							   	//console.log(html);
							    var wordcloud = $('#wordcloud');
							    wordcloud.attr('srcdoc',html);
							  }
							});
					}
				
					function ajax(shop_code){
						var num = document.getElementsByClassName('event_name').length;
						 $.ajax({
					            type :"POST",
					            url :"/pmkim/analysis",  
					            data : {"shop_code" : shop_code
					                   },
					            dataType : "json", 
					            success : function(data){	
					            	//shop name 클릭시 마다 변경
					            	document.getElementsByClassName('shop_name')[0].innerHTML=data[0].shop_name;
					            	document.getElementsByClassName('shop_name')[1].innerHTML=data[0].shop_name;
					            	
					            	//csv 읽고 그래프
					            	
					            	//상품 정보 받아와서 정보 뿌려주기
					               for(var i=0;i<num;i++){
					            	   document.getElementsByClassName('good_name')[i].innerHTML=data[i].good_name;
					            	   document.getElementsByClassName('good_price')[i].innerHTML=data[i].good_price+" 원";
					            	   document.getElementsByClassName('event_name')[i].innerHTML=data[i].event_name;
					            	   document.getElementsByClassName('box-img-hover')[i].innerHTML=
					            		   "<img src='"+data[i].good_img+"' class='img-fluid' alt='Image'>";
					               }
					        },
					        error : function(){
					           alert("프로그램 에러가 발생했습니다.2");
					        }
					     });
					}
					
					function graph(shop_code){
						var filecsv= "/pmkim/resources/csv/senti_data.csv";
						
						$.ajax({
							url: filecsv,
						  	dataType: "text",
						  	success: function(data){
						  		d3.csv(filecsv,function(error,data){
									//console.log(typeof data);
									//console.log(data);
									var dataSet = [ ];
									for(var i=0; i<data.length; i++){
										dataSet.push(data[i][shop_code]);
										//console.log(data[i][shop_code]);
									}
									
									
									var graph = d3.select("#myGraph")
										.selectAll("rect")
										.data(dataSet)
										.enter()
										.append("rect")
										.attr("x",60)
										.attr("y",function(d,i){
											return (i * 60);
										})
										.attr("height","50px")
										.attr("width", "0px");
									
									graph.transition()				
										.delay(function(d, i){
											return i * 1000;		
										})
										.duration(2500)			
										.attr("width", function(d, i){
											return d/3 +"px";		 
										});
									
									
									var text_data = ["LOVE : "+dataSet[0],"Negative : "+dataSet[1]];
									var text = d3.select("svg");
									//console.log(text);
									console.log(text_data);
									text.selectAll("text")
								    .data(text_data)
								    .enter().append("text")
								    .text(function(d) {return d})
								    .attr("class", "text")
								    .transition()				
									.delay(function(d, i){
										return i * 1000;		
									})
									.duration(4000)
								    .attr("x", 70)
								    .attr("y", function(d, i) {return 30+(i*60)})
								    ;
										
								});
						  }
						});
					}
					
					function feed(){
						var filecsv= "/pmkim/resources/csv/feed.csv";
						$.ajax({
							url: filecsv,
						  	dataType: "text",
						  	success: function(data){
						  		
						  		d3.csv(filecsv,function(error,data){
									var urlSet = [ ];
									var imgSet = [ ];
									for(var i=0; i<data.length; i++){
										urlSet.push(data[i].url);
										imgSet.push(data[i].img);
									}
									//var num = document.getElementsByClassName('ins-inner-box').length;
									for(var i =0; i<data.length;i++){
										document.getElementsByClassName('ins-inner-box')[i].innerHTML += 
											"<img src='"+imgSet[i]+"'/>"+
											"<div class='hov-in'><a href='"+urlSet[i]+
											"'><i class='fab fa-instagram'></i></a></div> ";
											if(data.length == 4){
												setTimeOut(function(){
													
												},1000);
											}
												
									}
									
									
									//ins-inner-box 400x400px
									//<div class="hov-in">
									//<a href="#"><i class="fab fa-instagram"></i></a>
									//
									
								});
						  }
						});
					}
					
					
					$(document).ready(function(){
						var shop_code = document.getElementsByClassName('shop')[0].id;
			               ajax(shop_code);
			               wordcloud(shop_code);
			               graph(shop_code);
			               feed();
						$("#next-carousel ").click(function(){
							// 그래프 지웟다가 다시 그리려면 svg 내용 지우고 넘겨야함 
							d3.selectAll("svg > *").remove();
                     //d3.selectAll(".ins-inner-box > *").remove();

							// 시간 지연해줘야 값 받아옴
							setTimeout(function(){
								//클릭하면 shop_code 받아오기
								shop_code = document.getElementsByClassName('carousel-item active')[0].id;
								
								ajax(shop_code);
							     wordcloud(shop_code);
							     graph(shop_code);
							},800);
						}); 
					});
					
				</script>
            
				
				<div class="col-xl-7 col-lg-7 col-md-6">
					<div class="single-product-details">

						<h2>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
						 DO YOU LOVE "<span class="shop_name"></span>" ? </h2>
						 <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
						 SNS 포스팅 감성분석 : <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
						 인스타그램 최신 게시물 5000 개를 감성 분석한 그래프
						 </p>
						 <svg id = "myGraph"></svg>
<!-- 						<div class="price-box-bar">
							<div class="cart-and-bay-btn">
								<a class="btn hvr-hover" data-fancybox-close="" href="#">Best 상품</a>
								
								<a class="btn hvr-hover" data-fancybox-close="" href="#">Best 상품 그래프</a>
								
								<a class="btn hvr-hover" data-fancybox-close="" href="#">감성분석 그래프</a>
							</div>
						</div> -->
					</div>
					
				</div>
						
			</div>
			
			

			<div class="row my-5">
				<div class="col-lg-12">
					<div class="title-all text-center">
						<h1>SNS 에서 가장 인기가 많은 <span class="shop_name"></span> 상품은?</h1>
						<p>최근 SNS 포스팅에서 가장 많이 노출된 상품 리스트</p>
					<p align="center" id="wordcloud_p">
			<iframe id="wordcloud" width = "100%" height = "350" srcdoc="" style="border:none">
			</iframe>
			</p>
					</div>
					
					<div class="featured-products-box owl-carousel owl-theme">
						<div class="item">
									<div class="type-lb">
                               		<p class="event_name"></p>
                           			</div>
							<div class="products-single fix">
								<div class="box-img-hover">
								<!-- image들어오는곳 -->
								</div>
								<div class="why-text">
									<h4 class="good_name"></h4>
									<h5 class="good_price"></h5>
								</div>
							</div>
						</div>
						<div class="item">
							<div class="type-lb">
                                <p class="event_name"></p>
                              </div>
                     <div class="products-single fix">
                        <div class="box-img-hover">
                           
                        </div>
                        <div class="why-text">
                           <h4 class="good_name"></h4>
                           <h5 class="good_price"></h5>
                        </div>
                     </div>
                  </div>
                  <div class="item">
                  <div class="type-lb">
                                <p class="event_name"></p>
                              </div>
                     <div class="type-lb">
                                <p class="event_name"></p>
                              </div>
                     <div class="products-single fix">
                        <div class="box-img-hover">
                           
                        </div>
                        <div class="why-text">
                           <h4 class="good_name"></h4>
                           <h5 class="good_price"></h5>
                        </div>
                     </div>
                  </div>
                  <div class="item">
                     <div class="type-lb">
                                <p class="event_name"></p>
                              </div>
                     <div class="products-single fix">
                        <div class="box-img-hover">
                           
                        </div>
                        <div class="why-text">
                           <h4 class="good_name"></h4>
                           <h5 class="good_price"></h5>
                        </div>
                     </div>
                  </div>
                  <div class="item">
                     <div class="type-lb">
                                <p class="event_name"></p>
                              </div>
                     <div class="products-single fix">
                        <div class="box-img-hover">
                           
                        </div>
                        <div class="why-text">
                           <h4 class="good_name"></h4>
                           <h5 class="good_price"></h5>
                        </div>
                     </div>
                  </div>
                  <div class="item">
                     <div class="type-lb">
                                <p class="event_name"></p>
                              </div>
                     <div class="products-single fix">
                        <div class="box-img-hover">
                           
                        </div>
                        <div class="why-text">
                           <h4 class="good_name"></h4>
                           <h5 class="good_price"></h5>
                        </div>
                     </div>
                  </div>
                  <div class="item">
                     <div class="type-lb">
                                <p class="event_name"></p>
                              </div>
                     <div class="products-single fix">
                        <div class="box-img-hover">
                           
                        </div>
                        <div class="why-text">
                           <h4 class="good_name"></h4>
                           <h5 class="good_price"></h5>
                        </div>
                     </div>
                  </div>
                  <div class="item">
                  <div class="type-lb">
                                <p class="event_name"></p>
                              </div>
                     <div class="products-single fix">
                        <div class="box-img-hover">
                        
                        </div>
                        <div class="why-text">
                           <h4 class="good_name"></h4>
                           <h5 class="good_price"></h5>
                        </div>
                     </div>
                  </div>
               </div>
            </div>
         </div>

      </div>
   </div>
   <!-- End Cart -->
	<!-- Start Instagram Feed  -->
	<div class="instagram-box">
		<div class="main-instagram owl-carousel owl-theme">
			<div class="item">
				<div class="ins-inner-box">
				</div>
			</div>
			<div class="item">
				<div class="ins-inner-box">
				</div>
			</div>
			<div class="item">
				<div class="ins-inner-box">
				</div>
			</div>
			<div class="item">
				<div class="ins-inner-box">
				</div>
			</div>
			<div class="item">
				<div class="ins-inner-box">
				</div>
			</div>
			<div class="item">
				<div class="ins-inner-box">
				</div>
			</div>
			<div class="item">
				<div class="ins-inner-box">
				</div>
			</div>
			<div class="item">
				<div class="ins-inner-box">
				</div>
			</div>
			<div class="item">
				<div class="ins-inner-box">
				</div>
			</div>
			<div class="item">
				<div class="ins-inner-box">
				</div>
			</div>
		</div>
	</div>
	<!-- End Instagram Feed  -->


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

   <!-- ALL JS FILES -->

   <script src="/pmkim/resources/js/popper.min.js"></script>
   <script src="/pmkim/resources/js/bootstrap.min.js"></script>
   <!-- ALL PLUGINS -->
   <script src="/pmkim/resources/js/jquery.superslides.min.js"></script>
   <script src="/pmkim/resources/js/bootstrap-select.js"></script>
   <script src="/pmkim/resources/js/inewsticker.js"></script>
   <script src="/pmkim/resources/js/bootsnav.js."></script>
   <script src="/pmkim/resources/js/images-loded.min.js"></script>
   <script src="/pmkim/resources/js/isotope.min.js"></script>
   <script src="/pmkim/resources/js/owl.carousel.min.js"></script>
   <script src="/pmkim/resources/js/baguetteBox.min.js"></script>
   <script src="/pmkim/resources/js/form-validator.min.js"></script>
   <script src="/pmkim/resources/js/contact-form-script.js"></script>
   <script src="/pmkim/resources/js/custom.js"></script>
   
</body>

</html>