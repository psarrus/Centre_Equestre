$(document).ready(function(){
    $('#table').DataTable({
        language: {
            "decimal":        "",
            "emptyTable":     "Le tableau est vide",
            "info":           "Lignes _START_ à _END_ sur _TOTAL_",
            "infoEmpty":      "Lignes 0 à 0 sur 0",
            "infoFiltered":   "(filtrées sur un total de _MAX_ lignes)",
            "infoPostFix":    "",
            "thousands":      ",",
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
                "sortAscending":  ": trier par ordre croissant",
                "sortDescending": ": trier par ordre décroissant"
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
});
