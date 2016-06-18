$(document).ready(function(){
    // PROFIL
    var permis    = $('#id_permis');
    var actif     = $('#id_profil_actif');

    permis.parent().parent().hide();

    if (actif.is(":checked")) {
        permis.parent().parent().show();
    }
    actif.change(function() {
        if (this.checked){
            permis.parent().parent().show();
            $('#id_permis').val(1);
         }else{
            permis.parent().parent().hide();
            $('#id_permis').val(0);
         }
    });
    // PROFIL FIN

    var table = $('#table').DataTable({
        dom: 'Bfrtip',
        buttons: [
            'copy', 'pdf', 'print'
        ],

        rowReorder: true,
        colReorder: true,
        fixedHeader: true,
        responsive: true,
        select: false,
        language: {
            "decimal":        ",",
            "emptyTable":     "Le tableau est vide",
            "info":           "Lignes _START_ à _END_ sur _TOTAL_",
            "infoEmpty":      "Lignes 0 à 0 sur 0",
            "infoFiltered":   "(filtrées sur un total de _MAX_ lignes)",
            "infoPostFix":    "",
            "thousands":      " ",
            "lengthMenu":     "Afficher _MENU_ lignes",
            "loadingRecords": "Chargement ...",
            "processing":     "Recherche ...",
            "search":         "Rechercher :",
            "zeroRecords":    "Aucune ligne trouvée",
            "paginate": {
                "first":      "Première page",
                "last":       "Dernière page",
                "next":       "Suivant",
                "previous":   "Précédent"
            },
            "aria": {
                "sortAscending":  "Trier par ordre croissant",
                "sortDescending": "Trier par ordre décroissant"
            }
        },

        initComplete: function () {
            this.api().columns().every( function () {
                var column = this;
                var select = $('<select class="form-control"><option value=""></option></select>')
                .appendTo( $(column.footer()).empty() )
                .on( 'change', function () {
                    var val = $.fn.dataTable.util.escapeRegex(
                        $(this).val()
                    );

                    column
                    .search( val ? '^'+val+'$' : '', true, false )
                    .draw();
                } );

                column.data().unique().sort().each( function ( d, j ) {
                    if ($(d).text() != ''){
                        d = $(d).text();
                     }
                    //console.log(d+' '+ $(d).text() );
                    select.append( '<option value="'+d+'">'+d+'</option>' );
                } );
            } );

        },
        // drawCallback: function () {
        //     var api = this.api();
        //     $( api.table().footer() ).html(
        //         api.column( 1, {page:'current'} ).data().sum()
        //     );
        // }
    });


    // $("#table tfoot th:nth-child(2)").html(table.column(1, {page:'current'} ).data().sum());



    function getCookie(name) {
       var cookieValue = null;
       if (document.cookie && document.cookie !== '') {
           var cookies = document.cookie.split(';');
           for (var i = 0; i < cookies.length; i++) {
               var cookie = jQuery.trim(cookies[i]);
               // Does this cookie string begin with the name we want?
               if (cookie.substring(0, name.length + 1) == (name + '=')) {
                   cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                   break;
               }
           }
       }
       return cookieValue;
   }

    $('input[name="my-checkbox"]').on('switchChange.bootstrapSwitch', function(event, state) {
      var id_cheval = $(this).val();
      var id_piquet = $(this).attr("piquet_staff");
      var id_creneau = $("#creneau_montoir").attr("id_montoir");
      console.log("cheval " + $(this).val() + " " + state + " id_piquet = " + id_piquet + " id_creneau = " + id_creneau);

        $.ajax({
          type: "POST",
          dataType: "html/json",
          url: "/monte/piquet/update/"+id_piquet+"/json",
          headers : {
               "HTTP_X_REQUESTED":'XMLHttpRequest',
               "X-CSRFToken" : getCookie('csrftoken'),
           },
          data: {cheval:id_cheval, montoir:id_creneau, selected:state},
          success: function(data) {
          },
          complete: function(data) {
          }
        });
    });


    $("[name='my-checkbox']").bootstrapSwitch();

});
