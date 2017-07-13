$(document).ready(function() {

    var site_address = "http://127.0.0.1:8080";
    var token = sessionStorage.getItem("token");

    $.urlParam = function (name) {
        var results = new RegExp('[\?&]' + name + '=([^&#]*)').exec(window.location.href);
        return results[1] || 0;
    };
    var id = $.urlParam('id');

    var settings = {
        "async": true,
        "crossDomain": true,
        "url": "http://ce419.herokuapp.com/blog/post?id=" + id,
        "method": "GET",
        "headers": {
            "x-token": token
        },
        "dataType": "json"
    };

    $.ajax(settings).done(function (response) {
        var x = "<img class=\"image\" src=\"img/" + ((id % 7) + 1) + ".png\" height=\"300\" width=\"200\"/>" +
            "<div class=\"title_and_summary\">" +
            "<h1 class=\"titlePage\">" + response.post.title + "</h1>" +
            "<h6 class=\"time\">" + convertDate(response.post.datetime) + "</h6>" +
            "</div>";
        var y = response.post.text;
        $(".detail").append(x);
        $(".info").append(y);
    });

    $(".show").on("click", function (event) {
         event.preventDefault();
         var comments=$(".comments");
        comments.empty();
        comments.show();
        loadComments();
    });
    $(".add").on("click", function (event) {
         event.preventDefault();
        $(".adding_comment_part").show();
    });
    $(".submit_comment").on("click",function (event) {
         event.preventDefault();
       var form = new FormData();
        form.append("post_id", id);
        form.append("text", $(".comment_text").val());
        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "http://ce419.herokuapp.com/blog/comment",
            "method": "POST",
            "headers": {
                "x-Token": token
            },
            "processData": false,
            "contentType": false,
            "mimeType": "multipart/form-data",
            "data": form,
            "dataType": "json"
        };
        $.ajax(settings).done(function (response) {
            console.log(response);
            if (response.status != "-1") {
                $(".comments").empty();
                loadComments();
                $(".adding_comment_part").hide();
            }
        });

    });
    $(".exit_comment").on("click", function (event) {
         event.preventDefault();
        $(".adding_comment_part").hide();
    });

    function loadComments(){
        var from = $(".from").val();
        var count = $(".count").val();
        var t ="?post_id="+id;
        var flag = false;
        if (count !== "")
            t = t+ "&count="+count;
        if (from !== "")
            t = t+ "&offset="+from;
        if(count === "" || count > 3)
            flag = true;


            var settings = {
                "async": true,
                "crossDomain": true,
                "url": "http://ce419.herokuapp.com/blog/comments" + t,
                "method": "GET",
                "headers": {
                    "x-token": token
                },
                "dataType": "json"
            };

            $.ajax(settings).done(function (response) {
                $.each(response.comments, function (index, element) {
                    var commentString = "<div class=\"comment\">" +
                        "<h4>Author</h4>" +
                        "<h6>" + convertDate(element.datetime) + "</h6>" +
                        "<p>" + element.text + " </p>" +
                        "</div>";
                    $('.comments').append(commentString)
                });
            });


        count -= 5;
        if(flag) {
            var win = $(window);
            var num = 0;
            var off = from + 5;
            win.scroll(function () {
                if ($(document).height() - win.height() == Math.floor(win.scrollTop()) && num < count ) {
                    //('.loading').show();
                    var settings = {
                        "async": true,
                        "crossDomain": true,
                        "url": "http://ce419.herokuapp.com/blog/comments" + t,
                        "method": "GET",
                        "headers": {
                            "x-token": token
                        },
                        "dataType": "json"
                    };

                    $.ajax(settings).done(function (response) {
                        $.each(response.comments, function (index, element) {
                    var commentString = "<div class=\"comment\">" +
                        "<h4>Author</h4>" +
                        "<h6>" + convertDate(element.datetime) + "</h6>" +
                        "<p>" + element.text + " </p>" +
                        "</div>";
                    $('.comments').append(commentString)
                });
                    });
                    num += 5;
                    off += 5;
                }
            });

        }

    };
});