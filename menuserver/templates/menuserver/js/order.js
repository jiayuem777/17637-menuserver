console.log("1");
$(document).ready(function(){
  $("#add-dish").click(function(){
    var name = $("#add-dish-name").val();
    var data = {'name' : name};
    console.log(data);

    $.post(
      // 请求的url
      '{% url 'ajax_post' %}',
      // 发送的数据
      data,
      // 回调函数，其中ret是返回的JSON，可以以字典的方式调用
      function(ret){
          var name = ret['name'];
          var number = ret['number'];
          var total_price = ret['total_price'];
          var exist = ret['exist'];

          if (exist == False) {
            var dishName = $("<h3>", {
              html: name,
              id: "dish-name"
              id = name
            });
            var dishNumber = $("<h3>", {
              html: number,
              id: "dish-number"
            });
            var newLine = $("<li>", {
              class: "order-line",
              id: name;
            })
            newLine.appendChild(dishName);
            newLine.appendChild(dishNumber);
            newLine.appendTo("#sidebar-ul");
          } else {
            var dishNum = document.getElementById(name).lastChild;
            dishNum.innerHTML = number;
          }
          $("#total_price").html("Total price:" + total_price + "$");

      });
    });


  });
