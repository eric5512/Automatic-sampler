#include "filehelper.h"

#define MANUAL    'M'
#define AUTOMATIC 'A'

float calc_total_size(int n_parts) {
    return (ROD_SIZE*n_parts+((int)(n_parts/2))*UNION_SIZE);
}


void FileHelper::create_manual_file(QString points, QString folder_name) {
    QStringList sl = points.replace('(', "").replace(')', "").replace(' ', "").split(',');

    if (sl.size() % 3 != 0)
        throw new std::runtime_error("Error parsing manual points");

    QFile file = QFile(folder_name+'/'+MOVEMENT_FILE);

    if (!file.open(QIODevice::WriteOnly))
        throw new std::runtime_error("Cannot open file");

    QDataStream out(&file);

    out << (char)MANUAL;

    for (const QString &s : sl) {
        bool ok;
        int next = s.toInt(&ok);
        if (!ok)
            throw new std::runtime_error("Cannot convert " + s.toStdString() + " to int");

        out << next;
    }

    file.close();
}


void FileHelper::create_automatic_file(quint16 points_x, quint16 points_y, quint16 points_z,
                                      QString folder_name) {
    if (points_x == 0 && points_y == 0 && points_z == 0) {
        throw new std::runtime_error("Must select at least 1 axis");
    }

    QFile file = QFile(folder_name+'/'+MOVEMENT_FILE);

    if (!file.open(QIODevice::WriteOnly))
        throw new std::runtime_error("Cannot open file");

    QDataStream out(&file);

    out << (char)AUTOMATIC;

    out << points_x
        << points_y
        << points_z; // Write the number of points

    file.close();
}


void FileHelper::read_sample_file(QString file_path, quint8** data) {
    QFile file = QFile(file_path);

    QDataStream in(&file);

    uint16_t points_x, points_y, points_z;

    in >> points_x >> points_y >> points_z;

    size_t total = points_x * points_y * points_z;

    *data = new quint8[total];
}
