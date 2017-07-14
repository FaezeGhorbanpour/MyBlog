$(document).ready(function() {
    var site_address = "http://127.0.0.1:8080";
    //console.log(site_address);
    $(".tab-group > li > a").click(function(event)
    {
        event.preventDefault();
		var active_tab_selector = $(".tab-group > li.active > a").attr("href");

		var actived_tab = $(".tab-group > li.active");
		actived_tab.removeClass("active");

		$(this).parents("li").addClass("active");

		$(active_tab_selector).removeClass("active");
		$(active_tab_selector).addClass("hide");

		var target_tab_selector = $(this).attr("href");
		$(target_tab_selector).removeClass("hide");
		$(target_tab_selector).addClass("active");
    });
    $(".sign").click(function (event) {
        event.preventDefault();
        $(".error").text("");
        var form = new FormData();
        var stid = $(".number").val();
        form.append("username",stid );
        var pass = $(".pass").val();
        var pass1 = $(".pass1").val();
        form.append("password1",pass);
        form.append("password2",pass1);
        form.append("first_name",$(".fname").val() );
        form.append("last_name",$(".lname").val());
        form.append("email",$(".email").val() );
         var settings = {
             "async": true,
             "crossDomain": true,
             "url": site_address + "/auth/register/",
             "method": "POST",
             "processData": false,
             "contentType": false,
             "mimeType": "multipart/form-data",
             "data": form,
             "dataType" : "json"
         };
        $.ajax(settings).done(function (response) {
              console.log('signing ... ');

             if(response.status === -1){
                    $(".error").text(Object.values(response.message));
             }
             else {
                 $(".number").val("");
                 $(".pass").val("");
                 $(".fname").val("");
                 $(".lname").val("");
                 $(".email").val("");
                 log_in(stid, pass);
             }
        });
    });
    $(".login").click(function (event) {
        event.preventDefault();
        var stid = $(".number2").val();
        var pass = $(".pass2").val();
        log_in(stid,pass);

    });

     function log_in (stid,pass) {
        var form = new FormData();
        form.append("username", stid);
        form.append("password", pass);
        var settings = {
            "async": true,
            "crossDomain": true,
            "url": site_address+"/auth/login/",
            "method": "POST",
            "processData": false,
            "contentType": false,
            "mimeType": "multipart/form-data",
            "data": form,
            "dataType": "json"
        };
        $.ajax(settings).done(function (response) {
            console.log('login ... ' );
              console.log(response);
            if (response.status === -1) {
                $(".error").text(response.message);
            }
            else {
                $(".number").val("");
                $(".pass2").val("");
                sessionStorage.setItem("token", response.token);
                console.log(response.token);
                window.open("main_page.html","_top");
            }
        });
    }


});