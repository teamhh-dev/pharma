
function removeRow(oButton) {
    var empTab = document.getElementById('myTable');
    console.log(oButton.parentNode.parentNode.rowIndex)
    empTab.deleteRow(oButton.parentNode.parentNode.rowIndex);
}

document.getElementById("addRow").addEventListener('click', function ()
{
    var table = document.getElementById("myTable")
    table.insertAdjacentHTML("afterbegin", " <tr>\n" +
        "                                        <td>\n" +
        "                                           <input class=\"inputInvoice\" list=\"inputInvoice\" type=\"text\" placeholder=\"Medicine Name\" style=\"width: 99%\">\n" +
        "                                            <datalist id=\"inputInvoice\">\n" +
        "                                                  <option value=\"Edge\">\n" +
        "                                                  <option value=\"Firefox\">\n" +
        "                                                  <option value=\"Chrome\">\n" +
        "                                                  <option value=\"Opera\">\n" +
        "                                                  <option value=\"Safari\">\n" +
        "                                            </datalist>\n" +
        "\n" +
        "                                        </td>\n" +
        "                                        <td>\n" +
        "                                            <input type=\"text\" class=\"inputInvoice\" style=\"width: 99%; background-color: #e9ecef\" disabled>\n" +
        "                                        </td>\n" +
        "                                        <td>\n" +
        "                                            <input type=\"text\" class=\"inputInvoice\" style=\"width: 99%;\">\n" +
        "                                        </td>\n" +
        "                                        <td>\n" +
        "                                            <input type=\"text\" class=\"inputInvoice\" style=\"width: 99%;\">\n" +
        "                                        </td>\n" +
        "                                        <td>\n" +
        "                                            <input type=\"text\" class=\"inputInvoice\" style=\"width: 99%\">\n" +
        "                                        </td>\n" +
        "                                        <td>\n" +
        "                                            <input type=\"text\" class=\"inputInvoice\" style=\"width: 99%;\">\n" +
        "                                        </td>\n" +
        "                                        <td>\n" +
        "                                            <input type=\"text\" class=\"inputInvoice\" style=\"width: 99%\">\n" +
        "                                        </td>\n" +
        "                                        <td>\n" +
        "                                            <input type=\"text\" class=\"inputInvoice\" style=\"width: 99%;\">\n" +
        "                                        </td>\n" +
        "                                        <td>\n" +
        "                                            <input type=\"text\" class=\"inputInvoice\" style=\"width: 99%; background-color: #e9ecef\" disabled>\n" +
        "                                        </td>\n" +
        "                                        <td>\n" +
        "                                            <input type=\"button\" class=\"deleteIcon\" class=\"delBtn\" onclick=\"removeRow(this)\" style=\"border: none;\">\n" +
        "                                        </td>\n" +
        "\n" +
        "                                    </tr>")


    var len = document.getElementsByClassName("invoice").item(0).offsetHeight
    len = document.getElementsByClassName("invoice").item(0).offsetHeight = len + 15;
    len = len+'px'
    document.getElementsByClassName("invoice").item(0).style.height = len;

})

