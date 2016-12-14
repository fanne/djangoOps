/**
 * Created by JYC103 on 2016/11/15.
 */

//选服时的全选反选操作
$(function () {
    //全选或全不选
    $("#all").click(function(){
        if(this.checked){
            $("#list :checkbox").prop("checked", true);
        }else{
            $("#list :checkbox").prop("checked", false);
        }
     });
    //全选
    $("#selectAll").click(function () {
         $("#list :checkbox,#all").prop("checked", true);
    });
    //全不选
    $("#unSelect").click(function () {
         $("#list :checkbox,#all").prop("checked", false);
    });
    //反选
    $("#reverse").click(function () {
         $("#list :checkbox").each(function () {
              $(this).prop("checked", !$(this).prop("checked"));
         });
         allchk();
    });

    //设置全选复选框
    $("#list :checkbox").click(function(){
        allchk();
    });

    //获取选中选项的值
    $("#getValue").click(function(){
        var valArr = new Array;
        $('input[name="dbcheckbox"]:checked').each(function(i){
            valArr[i] = $(this).val();
        });
        var vals = valArr.join(',');
          alert(vals);
    });
});
function allchk(){
    var chknum = $("#list :checkbox").size();//选项总个数
    var chk = 0;
    $("#list :checkbox").each(function () {
        if($(this).prop("checked")==true){
            chk++;
        }
    });
    if(chknum==chk){//全选
        $("#all").prop("checked",true);
    }else{//不全选
        $("#all").prop("checked",false);
    }
}


//添加新服
$(document).ready(function(){
    $("#addserverform").click(function(){
        newserver = $("#id_AddNum").val()
        if(confirm("确认添加新服"+newserver+"?")){
            return true;
        }else{
            return false;
        }
    })
})


//数据查询
//var xmlhttp
//if (windows.XMLHttpRequest)
//{
//    xmlhttp = new XMLHttpRequest();
//}
//else
//{
//    xmlhttp = new ActiveXObject("Microsoft.XMLHTTP")
//}




//获取添加新服表单值

$(document).ready(function(){
    $("#addserverform").submit(function(){
        console.log("dddd")
        $.ajax({
            type: "POST",
            url: "ow/addServer/",
            dataType: "json",
            data:{
                addnum:$("id_AddNum").val()
            },
            success:function(data){
                console.log("返回值："+data)
//                if(data.success){
//                    alert("获取输入值："+data.msg);
//                    console.log($("id_AddNum").val())
//                    console.log("qwqeqwe")
//                }
//                else{
//                    console.log($("id_AddNum").val());
//                }
            },
            error:function(data){
                console.log('ldldldldl')
            }
        })
    })
})


//$.ajax({
//    type:"POST",
//    url:"addServer",
//    data:$("#addserver-form").serialize(),
//    sucess:function(msg){alter(msg);},
//    error:function(error){alter(error);}
//})
