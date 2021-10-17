#include <iostream>

#include <windows.h>
#include <mmsystem.h>
#include <amaudio.h>

#pragma comment(lib, "winmm.lib")
using namespace std;




int main(int argc, char **argv)
{

    cout << "\n Winmm ! \n";



    PlaySound(TEXT("onEclateClubMixInedit.wav"), NULL, SND_FILENAME | SND_ASYNC);
    
    waveOutSetVolume(NULL, 0xFFFF);
    

    char stop;
    cin >> stop;

    PlaySound(NULL, 0, 0);

    cout << "end";
    return 0;
}
