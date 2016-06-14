$(document).ready(function(){
    // PROFIL
    var permis    = $('#id_permis');
    var perms     = $('.perm');
    var actif     = $('#id_profil_actif');
    var categorie = $("[id$='categorie']");
    var license   = $(".license");
    var publi     = $("[id$='public']");

    license.hide();
    permis.parent().parent().hide();

    if (actif.is(":checked")) {
        permis.parent().parent().show();
    }
    actif.change(function() {
        if (this.checked){
            permis.parent().parent().show();
            $('#id_permis').val(1);
            categorie.val(3);
            perms.hide();
         }else{
            permis.parent().parent().hide();
            $('#id_permis').val(0);
            categorie.val(0);
            perms.show();
            license.hide();
         }
    });

    permis.change(function() {
        var perm = $('#id_permis option:selected').text();
        if (perm === "Professeur") {
            categorie.val(3);
        }else if(perm === "Chef d'écurie"){
            categorie.val(4);
        }else{
            categorie.val(0);
        }
    });

    categorie.change(function() {
        var cat = $("[id$='categorie'] option:selected").text();
        if (cat === "Cavalier") {
            publi.val(2);
            license.show();
        }else if(cat === "Elève"){
            publi.val(1);
            license.hide();
        }else{
            publi.val(0);
            license.hide();
        }
    });

    publi.change(function() {
        var pub = $("[id$='public'] option:selected").text();
        if (pub === "Club") {
            license.show();
        }else{
            license.hide();
        }
    });
    // PROFIL FIN

    $('#table').DataTable({
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
                    select.append( '<option value="'+d+'">'+d+'</option>' );
                } );
            } );
        }
    });


    function getCookie(name) {
       var cookieValue = null;
       if (document.cookie && document.cookie != '') {
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
    //   console.log(this); // DOM element
      //console.log(event); // jQuery event
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
              console.log("ok");
          },
          complete: function(data) {
              console.log("complete\n"+data);
          }
        //   error: function(data) {
        //       console.log(data);
        //   }
        });


    });

    // $("[name='my-checkbox']").bootstrapSwitch();
});
