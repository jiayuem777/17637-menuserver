var increBtns = document.getElementsByClassName('increase-btn');
for (var i = 0; i < increBtns.length; i++) {
  increBtns[i].addEventListener('click', increase);
}

var decreBtns = document.getElementsByClassName('decrease-btn');
for (var i = 0; i < decreBtns.length; i++) {
  decreBtns[i].addEventListener('click', decrease);
}

$(".add-dish").click(function(){
  $.ajax({
    type:"POST",
    url:'{% url 'ajax_post' %}',
    data: {
      name: $(this).val(),
      csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
    },
    success:function(data){
      AddFunc(data);
    }

  });
});

function AddFunc(ret) {
  console.log(ret);
  var name = ret['name'];
  var number = ret['number'];
  var total_price = ret['total_price'];
  var exist = ret['exist'];

  if (!exist) {
    var dishName = document.createElement("span");
    var node1 = document.createTextNode(name);
    dishName.appendChild(node1);
    dishName.setAttribute("class", "dish-name");

    var br = document.createElement("br");

    var increaseBtn = document.createElement("button");
    increaseBtn.innerHTML = "+";
    increaseBtn.addEventListener('click', increase);
    increaseBtn.setAttribute("class", "btn btn-default increase-btn");
    increaseBtn.value = name;

    var dishNumber = document.createElement("span");
    var node2 = document.createTextNode(number);
    dishNumber.appendChild(node2);
    dishNumber.setAttribute("class", "dish-number");

    var decreaseBtn = document.createElement("button");
    decreaseBtn.innerHTML = "-";
    decreaseBtn.addEventListener('click', decrease);
    decreaseBtn.setAttribute("class", "btn btn-default decrease-btn");
    decreaseBtn.value = name;

    var hr = document.createElement("hr");

    var newLine = document.createElement("li");
    newLine.appendChild(dishName);
    newLine.appendChild(br);
    newLine.appendChild(increaseBtn);
    newLine.appendChild(dishNumber);
    newLine.appendChild(decreaseBtn);
    newLine.appendChild(hr);
    newLine.id = name;

    var sideul = document.getElementById("sidebar-ul");
    sideul.appendChild(newLine);

    console.log(newLine);
  } else {
    var li = document.getElementById(name);
    for (var i = 0; i < li.childNodes.length; i++) {
        if (li.childNodes[i].className == "dish-number") {
          var dishNum = li.childNodes[i];
          dishNum.innerHTML = number;
          break;
        }
    }
  }
  $("#total-price").html("Total price: " + total_price + "$");
}

function increase() {
  var increBtn = this;
  console.log(increBtn);
  $.ajax({
    type:"POST",
    url:'{% url 'ajax_increase' %}',
    data: {
      name: $(this).val(),
      csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
    },
    success:function(data){
      name = data['name'];
      number = data['number'];
      total_price = data['total_price'];
      var parentLi = increBtn.parentNode;
      for (var i = 0; i < parentLi.childNodes.length; i++) {
          if (parentLi.childNodes[i].className == "dish-number") {
            var spanNum = parentLi.childNodes[i];
            spanNum.innerHTML = number;
            break;
          }
      }
      $("#total-price").html("Total price: " + total_price + "$");
    }

  });
}

function decrease() {
  var decreBtn = this;
  $.ajax({
    type:"POST",
    url:'{% url 'ajax_decrease' %}',
    data: {
      name: $(this).val(),
      csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
    },
    success:function(data){
      name = data['name'];
      number = data['number'];
      disappear = data['disappear'];
      total_price = data['total_price'];
      var parentLi = decreBtn.parentNode;

      if (disappear) {
        var parentUl = parentLi.parentNode;
        parentUl.removeChild(parentLi);
      } else {
        for (var i = 0; i < parentLi.childNodes.length; i++) {
            if (parentLi.childNodes[i].className == "dish-number") {
              var spanNum = parentLi.childNodes[i];
              spanNum.innerHTML = number;
              break;
            }
        }
      }

      $("#total-price").html("Total price: " + total_price + "$");
    }

  });
}
