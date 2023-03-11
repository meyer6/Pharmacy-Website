from django.http import HttpResponse, HttpResponseRedirect
class Menu:
  def __init__(self, name, options = [], beforeFunc = None, afterFunc = None):
    self.name = name
    self.options = options
    self.beforeFunc = beforeFunc
    self.afterFunc = afterFunc

  def moveNode(self, destination):
    return HttpResponseRedirect('/main/'+self.options[destination].name.replace(" ", "")+"/")

  def addOptions(self, newOptions):
    self.options += newOptions
