/*
enable tooltip
separate js file because bootstrap states it has performance issues when applying to all pages
*/
$(function () {
    $("[data-toggle='tooltip']").tooltip();
});