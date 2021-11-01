#include "widget.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent)
{
    this->setStyleSheet("QLabel { background-color: yellow }");
    lab_hello->setText("helllo !");
}

Widget::~Widget()
{
    delete lab_hello;
}

