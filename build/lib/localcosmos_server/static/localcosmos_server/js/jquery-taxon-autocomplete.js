(function($) {
	$.fn.taxonautocomplete = function(options) {

		if (!options.hasOwnProperty("url")){
			throw new Error("taxonautocomplete requires options.url");
		}

		var taxon_verbose_input = $( this );

		var base_id = options["base_id"];
		
		// source and language of the search funtion (not the selected taxon)
		var search_taxon_source = $("#" + base_id + "_taxon_source");
		
		if (search_taxon_source.length){
			var search_taxon_source_value = search_taxon_source.val();
		}
		else {
			var search_taxon_source_value = "taxonomy.sources.col";
		}

		var language_input = $("#" + base_id + "_language");
		if (language_input.length){
			var language_input_value = language_input.val();
		}
		else {
			var language_input_value = "en";
		}

		var no_results_indicator = $("#" + base_id + "_info");
		
		// these are the input fields that are POST variables
		var taxon_source_input = $("#" + base_id + "_0");
		var taxon_latname_input = $("#" + base_id + "_1");
		var taxon_uuid_input = $("#" + base_id + "_2");
		var taxon_nuid_input = $("#" + base_id + "_3");


		// remove taxon values if key is pressed
		taxon_verbose_input.keyup(function(){
			taxon_source_input.val('');
			taxon_latname_input.val('');
			taxon_uuid_input.val('');
			taxon_nuid_input.val('');
		});
		
		// manage taxon_verbose input visual styles
		taxon_verbose_input.focusout(function(){

			no_results_indicator.hide();

			if (taxon_uuid_input.val().length == 0){
				taxon_verbose_input.val('');
				taxon_verbose_input.removeClass("is-valid");
			}
		});

		taxon_verbose_input.typeahead({
			autoSelect: false,
			source: function(input_value, process){

				taxon_verbose_input.removeClass("is-valid");

				$.ajax({
					type: "GET",
					url: options.url,
					dataType: "json",
					cache: false,
					data: {
						"searchtext": input_value,
						"language": language_input_value,
						"taxon_source": search_taxon_source_value
					},
					beforeSend : function(){
						no_results_indicator.hide();
					},
					success: function (data) {

						if (data.length == 0){
							no_results_indicator.show();
						}
						else {
							process($.map(data, function (item) {

								var taxon_object = {
									"name": item.label,
									"taxon_nuid": item.taxon_nuid,
									"taxon_latname": item.taxon_latname,
									"taxon_uuid": item.taxon_uuid,
									"taxon_source": item.taxon_source
								};

								return taxon_object;
							}));
						}
					},
					error: function(){
						
					}
				});
			}, 
			afterSelect : function(item){

				// set hidden input values
				taxon_source_input.val(item.taxon_source);
				taxon_latname_input.val(item.taxon_latname);
				taxon_uuid_input.val(item.taxon_uuid);
				taxon_nuid_input.val(item.taxon_nuid);

				// fire event on uuid input
				var event = new Event("change");
				var element = document.getElementById("" + base_id + "_2");
				element.dispatchEvent(event);
				
				taxon_verbose_input.addClass('is-valid');

				if (options.hasOwnProperty("afterSelect") && typeof(options.afterSelect) == 'function'){
					afterSelect(item);
				}

			},
			minLength: 3,
			delay: 500
		}); 
	}
}(jQuery));