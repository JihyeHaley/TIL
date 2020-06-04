

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
            
            
            $(document).ready(function(){
               var shop_code = document.getElementsByClassName('shop')[0].id;
                     ajax(shop_code);
                     
               $("#next-carousel ").click(function(){
                  // 시간 지연해줘야 값 받아옴
                  setTimeout(function(){
                     //클릭하면 shop_code 받아오기
                     shop_code = document.getElementsByClassName('carousel-item active')[0].id;
                       ajax(shop_code);
                      
                  },800);
               }); 
            });
