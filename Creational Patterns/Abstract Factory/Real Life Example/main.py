from __future__ import annotations
from abc import ABC, abstractmethod

class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_input(self) -> Input:
        pass



class WindowsUIFactory(UIFactory):
    def create_button(self) -> Button:
        return WindowsButton()
    def create_input(self) -> Input:
        return WindowsInput()
        
class WebUIFactory(UIFactory):
    def create_button(self) -> Button:
        return HTMLButton()
    def create_input(self) -> Input:
        return HTMLInput()


class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class Input(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class HTMLButton(Button):
    def render(self) -> str:
        return "HTMLButton rendered"

class WindowsButton(Button):
    def render(self) -> str:
        return "Windows Button rendered"

class HTMLInput(Input):
    def render(self) -> str:
        return "HTMLInput rendered"

class WindowsInput(Button):
    def render(self) -> str:
        return "Windows Input rendered"


def client_code(factory: UIFactory) -> None:
    button = factory.create_button()
    UIInput = factory.create_input()

    print(f"{button.render()}")
    print(f"{UIInput.render()}", end="")


if __name__ == "__main__":
    print("Client: Testing client code with the HTML factory:")
    client_code(WebUIFactory())

    print("\n")

    print("Client: Testing client code with the Windows factory:")
    client_code(WindowsUIFactory())