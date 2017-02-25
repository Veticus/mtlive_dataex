# mtlive-dataex

Allows the usage of the data available on live.midttrafik.dk in other projects.


### Prerequisites

To use this python 3.4 or above is needed.
The code is only tested on Python 3.4 on Linux and on Python 3.5.1 on OSX.

NB: This WILL NOT WORK on windows, in it's current form. This will, however, be changed later.

### Usage

As this is currently in a develop"mental" stage, running the .py file will only show information about the Line 100 of busses operated by Midttrafik. This may be boring. It is possible however to do exactly that, by running the python file as is.

On OSX:
```
python3 get_busdata.py
```

On Linux:
```
python get_busdata.py
```

CLA will be implemented at a later stage.

## Usage of the functions

By importing the get_busdata.py file, you can call the print_businfo_for_line() function.
It requires a line number to be given. Lines can be found here: [Midttrafik køreplaner](https://www.midttrafik.dk/koereplaner.aspx)

## Built With

* [Jetbrains PyCharm](https://www.jetbrains.com/pycharm/) - The IDE used. It's amazing!



## Authors

* **Tim Engel** - *Initial work* - [Veticus](https://github.com/Veticus)
* **Emil Madsen** - *xpath magician* - [Skeen](https://github.com/Skeen)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* I owe [Emil 'Skeen' Madsen](https://github.com/Skeen) a Club Mate, for helping me with the xpath.
* I owe [Mark 'Robotto' Moore](https://github.com/Robotto). I just can't remember what for. Sry.
* I owe JetBrains a collossal hug for allowing students the usage of their products free of charge <3