class Greeter:

    def __init__(self, input_name: str, input_place: str) -> None:
        # build an object contstructor that will store the input name and place
        # into object attributes for 'name' and 'place'.
        pass

    def greeting(self) -> None:
        # function to *print* a customized greeting greeting the person 
        # identified by the value in the 'name' attribute, and welcoming them 
        # to the value in the 'place' attribute
        pass

    def __str__(self) -> str:
        # implementaion for displaying the contents including name and place:
        return f'Name: {self.name}, Place: {self.place}'
        pass
