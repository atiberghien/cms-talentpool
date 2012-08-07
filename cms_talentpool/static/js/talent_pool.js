$(document).ready(function() { 
	$('#skill-choice-form input[type=submit]').remove();
	$('#skill-choice-form input[type=checkbox]').click(function(){
		$('#skill-choice-form').submit();
	});
	
	function activateEmbeddedDisplay(elmt) {
		elmt.click(function(){
	        $('#embedded-talent').load($(this).attr('href')+ " #talent", function(){
	        	activateEmbeddedDisplay($("#embedded-talent #talent a.display-talent"));
	        });
	        return false;
	    });
	}
	
	activateEmbeddedDisplay($('a.display-talent'));
    
    var options = { 
        target: '#main-people-mosaic',
        replaceTarget: true,
        clearForm: false,
        resetForm: false,
        success: function(){
        	$('#embedded-talent').children().remove();
        	activateEmbeddedDisplay($('a.display-talent'));
        },
    }; 
    
    $('#skill-choice-form').ajaxForm(options); 
    
    
    $('#talent-search-form').ajaxForm(options); 
    
}); 