#include "mainwindow.h"
#include "./ui_mainwindow.h"



MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow) {
    ui->setupUi(this);
    this->setWindowTitle("Automatic sampler");
    this->setWindowIcon(QIcon());
}

MainWindow::~MainWindow() {
    delete ui;
}

void MainWindow::on_actionExit_triggered() {
    close();
}

void MainWindow::on_graph_select_file_clicked() {
    QStringList file_names = QFileDialog::getOpenFileNames(this, tr("Open File"),"","");
    if (!file_names.empty())
        ui->graph_file_path->setText(file_names.first());
}


void MainWindow::on_button_generate_program_file_clicked() {
    QString folder_name = QFileDialog::getExistingDirectory(this);

    if (folder_name == "") return;

    try {
        if(ui->manual_reading->isChecked()) {
            FileHelper::create_manual_file(ui->manual_positions->toPlainText(), folder_name);
        } else {
            FileHelper::create_automatic_file(ui->check_box_x->isChecked() ? ui->spin_x_points->value() : 0,
                                             ui->check_box_y->isChecked() ? ui->spin_y_points->value() : 0,
                                             ui->check_box_z->isChecked() ? ui->spin_z_points->value() : 0,
                                             folder_name);
        }
    } catch(std::runtime_error *e) {
        QMessageBox::warning(this, "Error", e->what());
    }
}

void MainWindow::recalculate_total_points() {
    int total = (ui->check_box_x->isChecked() ? ui->spin_x_points->value() : 1) *
                (ui->check_box_y->isChecked() ? ui->spin_y_points->value() : 1) *
                (ui->check_box_z->isChecked() ? ui->spin_z_points->value() : 1);
    ui->spin_total_points->setValue(total);
}

void MainWindow::on_spin_x_points_valueChanged(int) {
    recalculate_total_points();
}


void MainWindow::on_spin_y_points_valueChanged(int) {
    recalculate_total_points();
}


void MainWindow::on_spin_z_points_valueChanged(int) {
    recalculate_total_points();
}


void MainWindow::on_check_box_x_stateChanged(int value) {
    ui->spin_x_points->setDisabled(!value);

    recalculate_total_points();
}


void MainWindow::on_check_box_y_stateChanged(int value) {
    ui->spin_y_points->setDisabled(!value);

    recalculate_total_points();
}


void MainWindow::on_check_box_z_stateChanged(int value) {
    ui->spin_z_points->setDisabled(!value);

    recalculate_total_points();
}


void MainWindow::on_generate_sensor_file_clicked() {
    // QString folder_name = QFileDialog::getExistingDirectory(this);

}


void MainWindow::on_manual_reading_stateChanged(int value) {
    ui->spin_x_points->setDisabled(value);
    ui->spin_y_points->setDisabled(value);
    ui->spin_z_points->setDisabled(value);

    ui->check_box_x->setDisabled(value);
    ui->check_box_y->setDisabled(value);
    ui->check_box_z->setDisabled(value);

    ui->spin_total_points->setDisabled(value);

    ui->manual_positions->setDisabled(!value);
}

