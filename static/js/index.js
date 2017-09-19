jQuery.expr[':'].icontains = function (a, i, m) {
    return jQuery(a).text().toUpperCase()
            .indexOf(m[3].toUpperCase()) >= 0;
};

$(document).ready(function () {
//     $('#carousel-example-generic').carousel({
//   interval: 2000
// })
    $('#searchPlatform').on('input', function (e) {
        var text = $(this).val().trim();
        refreshDataList(text)

    });
    $('.searchTags span').click(function (e) {
         var text = $(this).text().trim();
         $('#searchPlatform').val(text);
         refreshDataList(text);
    });

    function refreshDataList(text) {
        if ("" === text) {
            $(".bs-callout").removeClass('hidden');
        }

        $(".bs-callout:not(:icontains(" + text + "))").addClass('hidden');
        $(".bs-callout:icontains(" + text + ")").removeClass('hidden');
    }
});