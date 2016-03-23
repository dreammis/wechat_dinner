var product_count = 1;
var Total = 0;
var product_cost;
var product_settlement;
var product_name;
var product_String = "";

$(function(){
    $(".reduce").click(function(){
        product_reduce(this);
    })
    $(".add").click(function(){
        product_add(this);
    })
    $(".add_to_car").click(function(){
        var product = $(this).siblings();
        product_name = product.html();
        var product_Id = product.filter("input#productId").val();
        product_cost = parseFloat(product.next().html());
        product_settlement = product_cost * product_count;
        var tmp = $("#pId[value='" + product_Id + "']");
        if (tmp.length != 0) {
            var t = tmp.siblings();
            t.filter("input.PC").val(parseInt(t.filter("input.PC").val()) + parseInt(product_count));
            t.filter("input.PS").val((parseFloat(t.filter("input.PS").val()) + parseFloat(product_settlement)).toFixed(2));
        } else {
            var product_message = "<div class = 'P_message'>" +
            "<input class='PN' name='ProductName' type='text' readonly='readonly' value=" + product_name +">" +
            "<input class='Pcost' name='ProductCost' type='text' readonly='readonly' value=" + product_cost + ">" +
            "<span onclick='reduce(this)'>-</span>" +
            "<input class='PC' name='ProductCount' type='text' readonly='readonly' value='" + product_count + "'/>" +
            "<span onclick='add(this)'>+</span>" +
            "<input class='PS' name='ProductSettlement' type='text' readonly='readonly' value=" + product_settlement.toFixed(2) + ">" +
            "<div class='delete btn btn-sm btn-red waves-button waves-effect' onclick='product_Delete(this)'>取消</div>" +
            "<input type='hidden' id='pId' value='" + product_Id + "'/>" + "</div>";
            $("#CarList").append(product_message);
        }
        cost_sum();
        product_count = 1;
        product_Id = null;
        $(".productBox input").not("#productId").val(1);
    })
    $("#reset").click(function(){
        $("#CarList").empty();
        $("#cost_all").html("0.00")
    })
    $("#buy").click(function() {
        product_String = "";
        var msgs = $(".P_message");
        if (msgs.length == 0) {
            $(".modal-title").html("<span style='color:red;'>警告</span>");
            $(".modal-inner").html("<span style='color:red; font-size:20px;'>请选购货品后再进行支付！</span>");
        } else {
            $(".modal-title").html("微信扫一扫支付");
            $(".modal-inner").html("<div class='qrcodePanel' id='qrcodeTable' style='margin:0 auto; top:30px; width:350px; height:350px;'></div>");
            msgs.each(function(index, el) {
                var t_id = $(el).find("#pId").val();
                var t_count = $(el).find("input.PC").val();
                product_String += t_id + "*" + t_count + "_";
            });
            product_String = product_String.substring(0, product_String.length - 1);
            creatQrCode(product_String);
        }
    });
})

// create the QrCode
function creatQrCode(url){
    $("#qrcodeTable").html("");
    $("#qrcodeTable").qrcode({
        text    : url,
        width : "350",
        height : "350"
    });
}

function reduce(obj){
    product_reduce2(obj);
    var a = $(obj).prev().val();
    var b;
    b = a * product_count;
    $(obj).next().next().next().val(b.toFixed(2));
    cost_sum();
    product_count = 1;
    $(".productBox input").val(1);
}

function product_Delete(obj){
    obj.parentNode.parentNode.removeChild(obj.parentNode);
    cost_sum();
}

function add(obj){
    product_add(obj);
    var a = parseFloat($(obj).prev().prev().prev().val());
    var b;
    b = a * product_count;
    $(obj).next().val(b.toFixed(2));
    cost_sum();
    product_count = 1;
    $(".productBox input").val(1);
}

function product_add(obj){
    var P_input = $(obj).prev("input");
    var P_num = parseFloat(P_input.val());
    P_num = P_num + 1;
    P_input.val(P_num);
    product_count = P_num;
}

function product_reduce(obj){
    var P_input = $(obj).next("input");
    var P_num = parseFloat(P_input.val());
    if(P_num > 1){
        P_num = P_num - 1;
    }else if(P_num == 1){
        P_num = P_num;
    }
    P_input.val(P_num);
    product_count = P_num;
}

function product_reduce2(obj){
    var P_input = $(obj).next("input");
    var P_num = parseFloat(P_input.val());
    if(P_num > 1){
        P_num = P_num - 1;
    }else if(P_num == 1){
        product_Delete(obj);
    }
    P_input.val(P_num);
    product_count = P_num;
}

function cost_sum(){
    var getPrice=$(".PS");
    getPrice.each(function(i){
        Total += parseFloat(getPrice[i].value);
    })
    $("#cost_all").html(Total.toFixed(2));
    Total = 0;
}