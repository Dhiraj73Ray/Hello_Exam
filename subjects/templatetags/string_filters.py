from django import template

register = template.Library()

@register.filter
def before_parenthesis(value):
    return value.split('(')[0].strip()

@register.filter
def ext(value):
    """Return file extension from a filename"""
    if "." in value:
        return value.split(".")[-1].upper()  # e.g. PDF, DOCX
    return ""

@register.filter
def filename_only(value, start=13):
    """
    Return the file name (without extension), starting from `start` position.
    Example: "uploads/docs/12345_myfile.pdf" -> "myfile"
    """
    # Take substring starting from `start`
    name = value[start:]
    # Remove extension if present
    if "." in name:
        name = ".".join(name.split(".")[:-1])
    return name