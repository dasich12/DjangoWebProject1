$(document).ready(function () { //страница загружена    
    $('#SendComment').submit(Send); // цепляемся к форме
    Load(); //первичная загрузка комментариев       
    $("#loading").hide(); // ныкаем крутилку - прогрессбар
});
$(document).ajaxStart(function () { //подгрузка данных
    $("#loading").show();
    $("#comments").hide();
});
$(document).ajaxComplete(function () {//подгрузка данных - стоп
    $("#loading").hide();
    $("#comments").show();
});

function Load() { //загрузка комментариев
    $.ajax({
        type: "GET",
        url: "comment/",
        success: function (GetComments) {
            $("#comments").html(GetComments);
        }
    });
    return false;
}

function Send() {
    var FormData = $("#SendComment").serialize();
    $('#caption').val('');
    $('#commentText').val('');
    $.ajax({
        type: "POST",
        url: "comment/",
        data: FormData,
        success: function (postComment) {
            $("#comments").html(postComment);
        }
    });
    return false;
}