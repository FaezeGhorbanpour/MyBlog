var token = sessionStorage.getItem("token");
var site_address = "http://127.0.0.1:8080";
$(".goTo").click(function (event) {
    $(".menu>ul").attr("display", "block")
});
$(document).ready(function() {

   loadPosts(100,0);
    var action = true;
    $(".addPost").on("click", function (event) {
        event.preventDefault();
        if (action) {
            $(".over").show();
            action = false;
        }
        else {
            $(".over").hide();
            action = true;
        }
    });
    $(".exit").on("click", function (event) {
        window.open("StartPage.html", "_top");
    });

    $(".submit").on("click", function (event) {

        event.preventDefault();
        var form = new FormData();
        form.append("title", $(".title").val());
        form.append("summary", $(".summ").val());
        form.append("text", $(".text").val());
        var settings = {
            "async": true,
            "crossDomain": true,
            "url": site_address + "/blog/post",
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
            if (response.status === "-1") {
                $(".error").text(response.message);
            }
            else {
                $(".columns").empty();
                loadPosts(100,0);
                $(".over").hide();
                $(".title").val("");
                $(".summ").val("");
                $(".text").val("");
            }
        });
    });
});
function loadPost() {
     var settings = {
        "async": true,
        "crossDomain": true,
        "url": site_address + "/blog/posts?count=5&offset=0",
        "method": "GET",
        "headers": {
            "x-token": token
        },
        "dataType":"json"
    };

    $.ajax(settings).done(function (response) {
        $.each(response.posts, function(index, element) {
            var postString = "<div class=\"blog\" id=\"" +  element.id + "\"> \n" +
                "<img class=\"pic\" src=\"img/"+ ((element.id % 7)+1 ) +".png\"/>\n"+
                "<h1>"+element.title +"</h1>\n" +
                "<h6>" + convertDate(element.datetime) +"</h6>\n" +
                "<p class=\"summary\">"+element.summery +"</p>\n" +
                "<a href=\"Page.html?id="+element.id+"\">Read More</a>\n"+
                "</div>";
            $('.columns').append(postString)
        });
    });
}

function loadPosts(count,offset) {
loadPost();









    var win = $(window);
    var num = 0;
    var off = offset+5;
    win.scroll(function () {
        if ($(document).height() - win.height() === Math.floor(win.scrollTop()) && num < count && offset < 5) {
            //('.loading').show();
            var settings = {
                "async": true,
                "crossDomain": true,
                "url": site_address + "/blog/posts?count=5&offset=" + off,
                "method": "GET",
                "headers": {
                    "x-token": token
                },
                "dataType": "json"
            };

            $.ajax(settings).done(function (response) {
                $.each(response.posts, function (index, element) {
                    var postString = "<div class=\"blog\" id=\"" + element.id + "\"> \n" +
                        "<img class=\"pic\" src=\"img/" + ((element.id % 7) + 1 ) + ".png\"/>\n" +
                        "<h1>" + element.title + "</h1>\n" +
                        "<h6>" + convertDate(element.datetime) + "</h6>\n" +
                        "<p class=\"summary\">" + element.summery + "</p>\n" +
                        "<a href=\"Page.html?id=" + element.id + "\">Read More</a>\n" +
                        "</div>";
                    $('.columns').append(postString)
                });
            });
            num += 5;
            off += 5;
        }
    });

}