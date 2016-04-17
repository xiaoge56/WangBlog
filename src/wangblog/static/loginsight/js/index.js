$(document).ready(function() {
	$(".top-nav ul li").click(function(event) {
		$(this).addClass("active").siblings().removeClass("active");
	});
});

$('#pull').click(function(){
	$(".blackbox").fadeIn(function(){

	})
})

$(".file-acc1").click(function(){
	$(".file-acc01").show();
})

setTimeout(function(){
$('#new_tag').click();
}, 1000);


var n = 0;
$(document).scroll(function(){
	n=$(document).scrollTop();
  if(n>500){
	  $('#toTop').show();
	  }else{
	  $('#toTop').hide();
	}
})

$(function(){
	$('#toTop').click(function(){
		var pos = $(document).scrollTop();
		var delta = 1;
		var toTop = function(){
			if(pos + delta <=0){
				return;
			}
			setTimeout(function(){
				toTop();
			}, 20);
			$(document).scrollTop(pos);
			pos -= delta;
			delta *= 1.3;
		}
		toTop();
	});
/*$('#toTop').click(function(){
	$(window).scrollTop(0);
	$(window).animate({
		top:'0',
	})
})
*/

//$.validator.setDefaults({
//		submitHandler: function() {
//
//		}
//	});

jQuery.extend(jQuery.validator.messages, {
  required: "必选字段",
	remote: "请修正该字段",
	email: "请输入正确格式的电子邮件",
	url: "请输入合法的网址",
	date: "请输入合法的日期",
	dateISO: "请输入合法的日期 (ISO).",
	number: "请输入合法的数字",
	digits: "只能输入整数",
	creditcard: "请输入合法的信用卡号",
	equalTo: "请再次输入相同的值",
	accept: "请输入拥有合法后缀名的字符串",
	maxlength: jQuery.validator.format("请输入一个 长度最多是 {0} 的字符串"),
	minlength: jQuery.validator.format("请输入一个 长度最少是 {0} 的字符串"),
	rangelength: jQuery.validator.format("请输入 一个长度介于 {0} 和 {1} 之间的字符串"),
	range: jQuery.validator.format("请输入一个介于 {0} 和 {1} 之间的值"),
	max: jQuery.validator.format("请输入一个最大为{0} 的值"),
	min: jQuery.validator.format("请输入一个最小为{0} 的值")
});



		// validate signup form on keyup and submit
		$("#signupform").validate({

			rules: {
				username: "required",
				email: {
					required: true,
					email: true,
					remote: {
						url: "/checkemail",     //后台处理程序
						type: "get",               //数据发送方式
						dataType: "json",           //接受数据格式
						data: {                     //要传递的数据
							email: function () {
								return $("#email").val();
							}
						},
						dataFilter: function(data, type){
							if (data == "True"){
								return true;
							} else{
								return false;
							}
						}
					}
				},
				password: {
					required: true,
					minlength: 6
				},
				repassword: {
					required: true,
					minlength: 6,
					equalTo: "#password"
				},
				cellphone: {
          required: true,
          minlength: 11,
					remote: {
						url: "/checkphone",     //后台处理程序
						type: "get",               //数据发送方式
						dataType: "json",           //接受数据格式
						data: {                     //要传递的数据
							cellphone: function () {
								return $("#cellphone").val();
							}
						},
						dataFilter: function(data, type){
							if (data == "True"){
								return true;
							} else {
								return false;
							}
						}
					}
				},
				companyName: {
				    required: true,
						remote: {
							url: "/checkemail",     //后台处理程序
							type: "get",               //数据发送方式
							dataType: "json",           //接受数据格式
							data: {                     //要传递的数据
								companyName: function () {
									return $("#companyName").val();
								}
							},
							dataFilter: function(data, type){
								if (data == "True"){
									return true;
								} else{
									return false;
								}
							}
						}
				},
				servercnt : {
				    required: true,
				    maxlength: 2
				}
			},
			messages: {
				name: "请输入你的姓名",
				email: {
					required: "请输入您的邮箱",
                    email: "邮箱格式 XXX@yyyy.cc",
					remote: "邮箱已被注册"
				},
				password: {
					required: "为您的账户创建密码",
					minlength: "密码长度6-15位",
					maxlength: "密码长度6-15位"
				},
				repassword: {
					required: "重复输入您的密码",
					equalTo: "两次输入的密码不一致,请重新输入",
					minlength: "密码长度6-15位",
					maxlength: "密码长度6-15位"
				},
				cellphone: {
				    required: "输入您的手机号码",
				    maxlength: "手机号码为11位",
					minlength: "手机号码为11位",
					remote: "该手机号已被注册",
				},
				companyName: {
				    required: "输入公司或组织名称",
						remote: "该组织名已被注册"
				},
				servercnt: {
				    required: "请输入申请服务器数量",
				    maxlength: "服务器数量的最大不能超过2位数"
				}

			}
		});



//	$('#submit_btn').click(function(){
//	    var email = $("#email").val().trim()
//	    var password = $("#password").val().trim()
//	    var repassword = $("#repassword").val().trim()
//	    var company = $("#company").val().trim()
//	    var sever_cnt = $("#server_cnt").val().trim()
//	    var name  = $("name").val().trim()
//	    var phone = $("phone").val().trim()
//
//	});

});
