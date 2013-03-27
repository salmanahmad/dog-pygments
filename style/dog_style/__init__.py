from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Number, Operator, Generic, Whitespace


class DogStyle(Style):

    background_color = "#fff"
    default_style = ""

    styles = {
        Whitespace:                "#bbbbbb",
        Comment:                   "italic #5A525F",
        Comment.Preproc:           "noitalic",
        Comment.Special:           "noitalic bold",

        Keyword:                   "#811F24",
        Keyword.Pseudo:            "nobold",
        Keyword.Type:              "bold #00BB00",

        Operator:                  "#666666",
        Operator.Word:             "bold #AA22FF",

        Name.Builtin:              "#AA22FF",
        Name.Function:             "#234A97",
        Name.Class:                "#0000FF",
        Name.Namespace:            "bold #0000FF",
        Name.Exception:            "bold #D2413A",
        Name.Variable:             "#000",
        Name.Constant:             "#880000",
        Name.Label:                "#A0A000",
        Name.Entity:               "bold #999999",
        Name.Attribute:            "#BB4444",
        Name.Tag:                  "#0B6125",
        Name.Decorator:            "#AA22FF",

        String:                    "#0B6125",
        String.Doc:                "italic",
        String.Interpol:           "bold #BB6688",
        String.Escape:             "bold #BB6622",
        String.Regex:              "#BB6688",
        String.Symbol:             "#B8860B",
        String.Other:              "#008000",
        Number:                    "#811F24",

        Generic.Heading:           "bold #000080",
        Generic.Subheading:        "bold #800080",
        Generic.Deleted:           "#A00000",
        Generic.Inserted:          "#00A000",
        Generic.Error:             "#FF0000",
        Generic.Emph:              "italic",
        Generic.Strong:            "bold",
        Generic.Prompt:            "bold #000080",
        Generic.Output:            "#888",
        Generic.Traceback:         "#04D",

        Error:                     "border:#FF0000"
    }
