import xlsxwriter


def write2Excel(data, title, *args):
    """
    writes given matrix to an excel worksheet

    :param data: data matrix
    :param title: title of workbook and worksheet
    :param args: (optional) column and row name
    :return: excel workbook
    """

    path = "\\excel_results\\"

    # Create an new Excel file and add a worksheet.
    workbook = xlsxwriter.Workbook(path+title + '.xlsx')
    worksheet = workbook.add_worksheet(title)

    if len(args) == 0:

        i = 1
        j = 1
        for line in data:
            for value in line:
                worksheet.write(i, j, value)
                j += 1
            i += 1
            j = 1
    else:
        labels = args[0]

        # creating column titles
        for i in range(0, len(labels)):
            worksheet.write(0, i + 1, "T" + str(labels[i] + 1))

        for i in range(0, len(labels)):

            # creating row titles
            worksheet.write(i + 1, 0, "T" + str(labels[i] + 1))

            for j in range(0, len(labels)):
                worksheet.write(i + 1, j + 1, data[labels[i]][labels[j]])

#
# data = [[1, 2, 34, 5, 66, 5, 9, 2],
#         [1, 3, 34, 5, 66, 5, 3, 2],
#         [1, 2, 34, 5, 66, 5, 9, 2],
#         [1, 2, 34, 7, 76, 5, 9, 2],
#         [8, 7, 34, 5, 66, 3, 9, 2],
#         [1, 2, 34, 5, 66, 5, 1, 2],
#         [1, 2, 34, 5, 66, 5, 9, 2],
#         [1, 2, 34, 5, 66, 5, 9, 2]
#         ]
# label = [3, 5, 7]
# write2Excel(data, 'test', label)
