import flet as ft
from UI.view import View
from model.modello import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
    def handleYears(self):
        for anno in self._model.getYears():
            self._view.ddyear.options.append(ft.dropdown.Option(key=str(anno), text=str(anno)))
        self._view.update_page()
    def handleShapes(self, e):
        anno = self._view.ddyear.value
        shapes = self._model.getShapes(anno)
        for shape in shapes:
            self._view.ddshape.options.append(ft.dropdown.Option(key=str(shape), text=str(shape)))
        self._view.update_page()
    def handle_graph(self, e):
        self._view.controls.clear()
        anno = self._view.ddyear.value
        shape = self._view.ddshape.value
        if anno is None or shape is None:
            self._view.txt_result1.controls.append(ft.Text("Errore! seleziona prima anno e shape", color="red"))
            self._view.update_page()
            return
        self._view.controls.clear()
        self._model.buildGraph(anno, shape)
        self._view.txt_result1.controls.append(ft.Text(f"Grafo creato!\nN.nodi:{self._model.details()[0]}\nN.archi:{self._model.details()[1]}"))
        for n1,n2,peso in self._model.get_top5_archi():
            self._view.txt_result1.controls.append(ft.Text(f"nodo partenza: {n1.id} - nodo arrivo: {n2.id} - peso: {peso}"))

        self._view.update_page()

    def handle_path(self, e):
        pass
