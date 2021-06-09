function updateTable() {
    $.ajax({
        type: "GET",
        url: "getAllMedicines",

        success: function(response) {
            // $("table-body").;
            $(".table-body").empty();

            for (let i = 0; i < response.length; i++) {
                let row = response[i];

                var content = '<tr id="' + row.id + '">' + "<td>" + row.name + "</td>" + "<td>" + row.category + "</td>" + "<td>" + row.unit + "</td>" + "<td>" + row.details + "</td>" + "<td>" + row.price + "</td>" + "<td>" + row.manufacturer_name + "</td>" + "<td>" + row.manufacturer_price + "</td>" + '<td><img src="/static/medicine-images/' + row.image + '"' + ' class="medicine-image" alt="No Image!"></td>' + '<td><button class="btn" onclick="deleteMedicine(this.parentNode.parentNode.id)"><i class="fa fa-trash fa-2x"></i></button><button class="btn" onclick="updateMedicine(this.parentNode.parentNode.id)"><i class="fa fa-edit fa-2x"></i></button></td></tr>';
                $(".table-body").append(content);
            }

        }
    });

}

function hideUpdateContainer() {
    document.getElementsByClassName("update-container")[0].classList.toggle("hide");
    document.getElementsByClassName("container")[0].classList.toggle("hide");

}

function deleteMedicine(params) {
    var flag = confirm("Are Your Sure You Want To Delete Medicine!");
    var urlMethod = "deleteMedicine";
    dataToSend = { id: params }
    if (flag) {

        $.ajax({
            type: "DELETE",
            url: urlMethod,
            data: dataToSend,
            success: function(response) {
                alert("Deleted!")
                console.log(response);
                updateTable();
            }
        });


    }

}

function updateMedicine(params) {
    var medicine = null;
    urlMethod = "getMedicine";
    dataToSend = { id: params };
    // var medicineName = document.getElementsByName("name")[0].value;
    // var medicineCategory = document.getElementsByName("category")[0].value;
    // var medicineUnit = document.getElementsByName("unit")[0].value
    // var medicineDetails = document.getElementsByName("details")[0].value
    // var medicinePrice = document.getElementsByName("price")[0].value
    // var manufacturername = document.getElementsByName("manufacturername")[0].value
    // var manufacturerprice = document.getElementsByName("manufacturerprice")[0].value
    // var image = document.getElementsByName("image")[0].value
    $.ajax({
        type: "GET",
        url: urlMethod,
        data: dataToSend,
        success: function(response) {
            medicine = response;
            console.log(response)

            var image = document.getElementsByName("image")[0].value;
            console.log(image)
            document.getElementsByName("ide")[0].value = medicine.id;
            document.getElementsByName("name")[0].value = medicine.name;
            document.getElementsByName("category")[0].value = medicine.category;
            document.getElementsByName("unit")[0].value = medicine.unit;
            document.getElementsByName("details")[0].value = medicine.details;
            document.getElementsByName("price")[0].value = medicine.price;
            document.getElementsByName("manufacturername")[0].value = medicine.manufacturer_name;
            document.getElementsByName("manufacturerprice")[0].value = medicine.manufacturer_price;

        }
    });
    // $("").click(function(e) {
    //     e.preventDefault();

    // });
    // $(document).on("click", "#update_data", function() {
    //     console.log("clicked update");
    //     $.ajax({
    //         type: "PUT",
    //         url: "updateMedicine",
    //         data: new FormData(this),
    //         success: function(response) {
    //             console.log(response)
    //         }
    //     });

    // });
    console.log("update", params);
    document.getElementsByClassName("container")[0].classList.toggle("hide");
    document.getElementsByClassName("update-container")[0].classList.toggle("hide");
    // console.log(medicine.name)

    console.log(document.getElementsByName("name")[0]);
}