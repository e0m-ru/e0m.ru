const dropZone = document.getElementById('drag-and-drop-zone');
dropZone.addEventListener('dragover', function(e) {
e.preventDefault();
this.className = 'drop-zone dragover';
});
dropZone.addEventListener('dragleave', function(e) {
e.preventDefault();
this.className = 'drop-zone';
});
dropZone.addEventListener('drop', function(e) {
e.preventDefault();
this.className = 'drop-zone';
// Обработка файлов
let files = e.dataTransfer.files;
console.log(files);
});
