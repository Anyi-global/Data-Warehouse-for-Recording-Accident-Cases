$(document).ready(function() {
    const dropzone = $('#dropzone');
    const fileInput = $('#fileInput');
    const uploadHistory = $('#uploadHistory');

    dropzone.on('click', function() {
        fileInput.click();
    });

    fileInput.on('change', function(event) {
        handleFiles(event.target.files);
    });

    dropzone.on('dragover', function(event) {
        event.preventDefault();
        event.stopPropagation();
        dropzone.addClass('dragover');
    });

    dropzone.on('dragleave', function(event) {
        event.preventDefault();
        event.stopPropagation();
        dropzone.removeClass('dragover');
    });

    dropzone.on('drop', function(event) {
        event.preventDefault();
        event.stopPropagation();
        dropzone.removeClass('dragover');
        const files = event.originalEvent.dataTransfer.files;
        handleFiles(files);
    });

    function handleFiles(files) {
        for (let file of files) {
            uploadFile(file);
        }
    }

    function uploadFile(file) {
        const formData = new FormData();
        formData.append('file', file);

        const listItem = $('<li></li>');
        const fileName = $('<span></span>').text(file.name);
        const progressBar = $('<div class="progress"></div>').append('<div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar"></div>');
        const percent = $('<span class="percent">0%</span>');
        const checkmark = $('<i class="fas fa-check checkmark" style="display: none;"></i>');
        listItem.append(fileName).append(progressBar).append(percent).append(checkmark);
        uploadHistory.append(listItem);

        $.ajax({
            url: '/file_uploads', // Your server-side upload script
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            xhr: function() {
                const xhr = new window.XMLHttpRequest();
                xhr.upload.addEventListener('progress', function(event) {
                    if (event.lengthComputable) {
                        const percentComplete = (event.loaded / event.total) * 100;
                        progressBar.find('.progress-bar').css('width', percentComplete + '%').attr('aria-valuenow', percentComplete);
                        percent.text(Math.round(percentComplete) + '%');
                    }
                }, false);
                return xhr;
            },
            success: function(response) {
                progressBar.find('.progress-bar').removeClass('progress-bar-animated').addClass('bg-success');
                percent.show();
                checkmark.show();
            },
            error: function() {
                progressBar.find('.progress-bar').removeClass('progress-bar-animated').addClass('bg-danger');
            }
        });
    }
});
