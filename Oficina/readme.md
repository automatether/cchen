# AppOffice

#### Modo de uso
El programa puede ser ejecutado directamente utilizando python 3. En caso de no tenerlo instalado, se puede descargar [aqui](https://www.python.org/downloads/).

<br/>

Para instalar las dependencias mediante el gestor de paquetes de python (pip):

`pip install paramiko pymongo numpy pandas tkinter pyqt5 pyqtgraph`

<br/>

Luego para ejecutar:

`python AppOffice.py`

<br/>

El software puede ser complilado a programa de windows (.exe) utilizando [pyinstaller](https://pyinstaller.org/en/stable/):

`pyinstaller AppOffice.py --icon icon.ico --windowed`

<br/>

Posteriormente se puede agregar el archivo 'icon.ico' a la carpeta generada y crear un acceso directo a AppOffice.exe para mayor comodidad.