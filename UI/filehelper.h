#ifndef FILEHELPER_H
#define FILEHELPER_H

#include "constants.h"
#include <QString>
#include <QFile>
#include <QException>
#include <iostream>

class FileHelper
{
public:
    FileHelper();
    static void create_automatic_file(quint16 points_x, quint16 points_y, quint16 points_z,
                                     QString folder_name);

    static void create_manual_file(QString points, QString folder_name);

    static void read_sample_file(QString file_path, quint8** data);
};

#endif // FILEHELPER_H
