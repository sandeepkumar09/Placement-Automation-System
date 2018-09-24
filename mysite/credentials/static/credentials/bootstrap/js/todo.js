var todo = todo || {},
		data = JSON.parse(localStorage.getItem("todoData"));

data = data || {};

(function(todo, data, $) {

	var defaults = {
			todoTask: "todo-task",
			todoHeader: "task-header",
			todoDate: "task-date",
			todoDescription: "task-description",
			taskId: "task-",
			formId: "todo-form",
			dataAttribute: "data",
			deleteDiv: "delete-div"
		},
	  codes = {
	  	"1" : "#pending",
	  	"2" : "#inProgress",
	  	"3" : "#completed"
	  };

	todo.init = function (options) {

		options = options || {};
		options = $.extend({}, defaults, options);

		$.each(data, function (index, params) {
			generateElement(params);
		});

		$.each(codes, function (index,value){
			$(value).droppable({
				drop: function (event, ui) {
					var element = ui.helper,
							css_id = element.attr("id"),
							id = css_id.replace(options.taskId, ""),
							object = data[id];

					console.log(data[id]);

					removeElement(object);

					object.code = index;

					generateElement(object);

					data[id] = object;
					localStorage.setItem("todoData", JSON.stringify(data));

					$("#" + defaults.deleteDiv).hide();
				}
			});
		});

		$("#" + options.deleteDiv).droppable({
			drop: function(event, ui) {
				var element = ui.helper,
						css_id = element.attr("id"),
						id = css_id.replace(options.taskId, ""),
						object = data[id];

				removeElement(object);

				delete data[id];
				localStorage.setItem("todoData", JSON.stringify(data));

				$("#" + defaults.deleteDiv).hide();
			}
		});
	};


	//Add Task
	var generateElement = function(params) {
		var parent = $(codes[params.code]),
				wrapper,
				wrapperTitle,
				wrapperDescription,
				wrapperDate;

		console.log(parent);

		if (!parent)
			return;

		wrapper = $("<div />", {
			"class" : defaults.todoTask,
			"id" : defaults.taskId + params.id,
			"data" : params.id
		}).appendTo(parent);

		wrapper.draggable({
			start: function() {
				$("#" + defaults.deleteDiv).show();
			},
			stop: function() {
				$("#" + defaults.deleteDiv).hide();
			}
		});


		wrapperTitle = $("<div />", {
			"class" : defaults.todoHeader,
			"text" : params.title
		}).appendTo(wrapper);

		wrapperDate = $("<div />", {
			"class" : defaults.todoDate,
			"text" : params.date
		}).appendTo(wrapper);

		wrapperDescription = $("<div />", {
			"class" : defaults.todoDescription,
			"text" : params.description
		}).appendTo(wrapper);

	};

	// Deleting Tasks
	var removeElement = function(params) {
		$("#" + defaults.taskId + params.id).remove();
	};

	// Form
	todo.add = function() {
		var inputs = $("#" + defaults.formId + " :input"),
				errorMessage = "Title can not be empty",
				id,
				title,
				description,
				date,
				tempData;

		if (inputs.length !==4)
			return;

		title = inputs[0].value;
		description = inputs[1].value;
		date = inputs[2].value;

		if (!title) {
			generateDialog(errorMessage);
			return;
		}

		id = new Date().getTime();

		tempData = {
			id: id,
			code: "1",
			title: title,
			date: date,
			description: description
		};

		//Saving element in local storage
		data[id] = tempData;
		localStorage.setItem("todoData", JSON.stringify(data));

		//Generate Todo Element
		generateElement(tempData);

		//Reset Form
		inputs[0].value = "";
		inputs[1].value = "";
		inputs[2].value = "";

	};

	var generateDialog = function (message) {
		var responseId = "response-dialog",
				title = "Message",
				responseDialog = $("#" + responseId),
				buttonOptions;

		if (!responseDialog.length) {
			responseDialog = $("<div />", {
				title: title,
				id: responseId
			}).appendTo($("body"));
		}

		responseDialog.html(message);

		buttonOptions = {
			"Ok" : function () {
				responseDialog.dialog("close");
			}
		};

		responseDialog.dialog({
			autoOpen: true,
			width: 400,
			modal: true,
			closeOnEscape: true,
			buttons: buttonOptions
		});
	};

	todo.clear = function () {
		data = {};
		localStorage.setItem("todoData", JSON.stringify(data));
		$("." + defaults.todoTask).remove();
	};

})(todo, data, jQuery);
