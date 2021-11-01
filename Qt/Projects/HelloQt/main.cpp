#include "widget.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    Widget mainWidget;
    mainWidget.show();
    return app.exec();
}
