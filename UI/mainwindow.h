#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QFileDialog>
#include <QMessageBox>
#include <iostream>
#include "filehelper.h"

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_actionExit_triggered();

    void on_graph_select_file_clicked();

    void on_button_generate_program_file_clicked();

    void on_spin_x_points_valueChanged(int arg1);

    void on_spin_y_points_valueChanged(int arg1);

    void on_spin_z_points_valueChanged(int arg1);

    void on_check_box_x_stateChanged(int arg1);

    void on_check_box_y_stateChanged(int arg1);

    void on_check_box_z_stateChanged(int arg1);

    void on_generate_sensor_file_clicked();

    void on_actionLoad_config_file_triggered();

    void on_manual_reading_stateChanged(int arg1);

private:
    Ui::MainWindow *ui;
    void recalculate_total_points();
};
#endif // MAINWINDOW_H
