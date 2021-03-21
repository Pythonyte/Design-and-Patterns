"""
Provide an interface for creating families of related or dependent objects without specifying their concrete classes.


families of related or dependent objects:
    Button : MacButton, LinuxButton, WindowButton
    CheckBox : MacCheckBox, LinuxCheckBox, WindowCheckBox
    Label: MacLabel, LinuxLabel, WindowLabel
    
Factories:
    WindowUIFactory: Interface to create window type of objects
    MacUIFactory:Interface to create Mac type of objects
    LinuxUIFactory: Interface to create Linux type of objects
"""
from abc import ABCMeta, abstractmethod

## Products
class Button(metaclass=ABCMeta):
    def __init__(self, size=1):
        self.size = size
    @abstractmethod
    def display(self):
        pass

class MacButton(Button):
    def display(self):
        print("{} Button {}".format('!'*self.size, '!'*self.size))

class WindowButton(Button):
    def display(self):
        print("{} Button {}".format('$'*self.size, '$'*self.size))
        
class LinuxButton(Button):
    def display(self):
        print("{} Button {}".format('#'*self.size, '#'*self.size))


class CheckBox(metaclass=ABCMeta):
    def __init__(self, size=1):
        self.size = size

    @abstractmethod
    def display(self):
        pass

class MacCheckBox(CheckBox):
    def display(self):
        print("{} CheckBox {}".format('!' * self.size, '!' * self.size))

class WindowCheckBox(CheckBox):
    def display(self):
        print("{} CheckBox {}".format('$' * self.size, '$' * self.size))


class LinuxCheckBox(CheckBox):
    def display(self):
        print("{} CheckBox {}".format('#' * self.size, '#' * self.size))

class Label(metaclass=ABCMeta):
    def __init__(self, size=1):
        self.size = size

    @abstractmethod
    def display(self):
        pass

class MacLabel(Label):
    def display(self):
        print("{} Label {}".format('!' * self.size, '!' * self.size))


class WindowLabel(Label):
    def display(self):
        print("{} Label {}".format('$' * self.size, '$' * self.size))


class LinuxLabel(Label):
    def display(self):
        print("{} Label {}".format('#' * self.size, '#' * self.size))

## Factories
class UIFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_button(self):
        pass
    @abstractmethod
    def create_label(self):
        pass
    @abstractmethod
    def create_checkbox(self):
        pass


class MacFactory(UIFactory):
    def create_button(self):
        self.button = MacButton()
    def create_label(self):
        self.label = MacLabel()
    def create_checkbox(self):
        self.checkbox = MacCheckBox()

class WindowFactory(UIFactory):
    def create_button(self):
        self.button = WindowButton()
    def create_label(self):
        self.label = WindowLabel()
    def create_checkbox(self):
        self.checkbox = WindowCheckBox()

class LinuxFactory(UIFactory):
    def create_button(self):
        self.button = LinuxButton()
    def create_label(self):
        self.label = LinuxLabel()
    def create_checkbox(self):
        self.checkbox = LinuxCheckBox()




if __name__ == '__main__':


    wf = WindowFactory()
    lf = LinuxFactory()
    mf = MacFactory()

    def display(factory_obj):
        factory_obj.create_button()
        factory_obj.create_label()
        factory_obj.create_checkbox()
        factory_obj.button.display()
        factory_obj.label.display()
        factory_obj.checkbox.display()

    display(mf)
    display(lf)
    display(wf)




#### OUTPUT
! Button !
! Label !
! CheckBox !
# Button #
# Label #
# CheckBox #
$ Button $
$ Label $
$ CheckBox $
