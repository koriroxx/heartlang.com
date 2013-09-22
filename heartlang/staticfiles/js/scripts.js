//Pass through the element that triggers the fading;
//Pass through the element that is to be faded (child of the trigger)
//eg: <div class="hoverElement"><span class="tooltipElement">text</span></div>
//Strings passed are jQuery DOM calls, eg fadeInOut(".hoverElement", "tooltipElement");
function tooltip(hoverElement, tooltipElement) {
	$(hoverElement).hover(function() {
		$(tooltipElement, this).animate({
			opacity: 1,
			marginTop: "-75px",
		}, 500, function () {
			//stuff to do when the element has been faded in
		});

		$(hoverElement).mouseleave(function() {
				$(tooltipElement, this).animate({
					opacity: 0,
					marginTop: "-125px",
				}, 500, function () {
					//delete the element once faded out
					$(this).remove();
				});
			});
	});
}
		
		
//Pass through a message into a pop-up element
function statusMessage(messageText, type) {
	$("#content").append("<div class='message' style='opacity: 0'><span class='messagetext'></span><span class='close'>Close</span></div>");
	$(".message .messagetext").text(messageText);
	$(".message").animate({
		opacity: 1,
	}, 1500, function () {
		
		$(".close").click(function () {
			$(".message").fadeOut('slow', function() {
				//delete the element once faded out
				$(this).remove();
			});
		});
	});
}