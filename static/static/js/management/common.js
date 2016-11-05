$(".select-all-checkbox").click(function(){
	$(".select-checkbox").each(function () {
        if ($('.select-all-checkbox').prop('checked')) {
            $(this).prop('checked', true);
        } else {
            $(this).prop('checked', false);
        }
    });
});


function spawnBasicNotification(theBody, theIcon, theTitle){
    var options = {
        body: theBody,
        icon: theIcon
    };
    var n = new Notification(theTitle, options);
    setTimeout(n.close.bind(n), 5000);
}

