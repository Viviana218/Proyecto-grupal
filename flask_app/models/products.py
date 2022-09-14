from flask_app.config.mysqlconnection import  connectToMySQL

class Product:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.p_sale = data['p_sale']
        self.presentation = data['presentation']
        self.price = data['price']
        self.image = data ['image']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.cultivators_id = data['cultivators_id']
        #self.cultivators_name = data['full_name']

    """@staticmethod
    def valida_crop(formulario):
        es_valido = True 

        errores=[]
        
        if formulario['farm'] == "":
            errores.append('Debe ingresar el nombre de la finca')
            es_valido = False

        if formulario['state'] == "":
            errores.append('Debe ingresar el nombre del departamento')
            es_valido = False

        if formulario['municipality'] == "":
            errores.append('Debe ingresar el nombre del municipio')
            es_valido = False
        
        if formulario['fertilizer'] == "":
            errores.append('Debe ingresar el nombre del municipio')
            es_valido = False
        
        if formulario['f_amount'] == "":
            errores.append('Debe ingresar la cantidad de fertilizante')
            es_valido = False
        
        if formulario['date'] == "":
            errores.append('Debe ingresar la fecha de cosecha')
            es_valido = False

        if formulario['production'] == "":
            errores.append('Debe ingresar la produccion de su cosecha')
            es_valido = False

        if formulario['description'] == "":
            errores.append('Debe ingresar una descripcion')
            es_valido = False

        if formulario['image'] == "":
            errores.append('Debe ingresar una imagen')
            es_valido = False

        if formulario['share'] == "":
            errores.append('Debe seleccionar si desea compartir')
            es_valido = False
        
        return (es_valido, errores)"""


    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO products (name, description, p_sale, presentation, price, image, cultivators_id) VALUES (%(name)s, %(description)s, %(p_sale)s, %(presentation)s,%(price)s, %(image)s, %(cultivators_id)s)"
        result = connectToMySQL('weedproject').query_db(query, formulario)
        return result

    @classmethod
    def get_all(cls,formulario):
        query = "SELECT products.*, name FROM products LEFT JOIN cultivators ON cultivators.id = products.cultivators_id"
        results = connectToMySQL('weedproject').query_db(query,formulario) 
        products = []
        for product in results:
            
            products.append(cls(product)) 

        return products

    @classmethod
    def get_all_for_buyers(cls):
        query = "SELECT * FROM products"
        results = connectToMySQL('weedproject').query_db(query) 
        products = []
        for product in results:
            products.append(cls(product)) 
        return products

    @classmethod
    def get_by_id(cls, formulario): 
        query = "SELECT products.*, name FROM products LEFT JOIN cultivators ON cultivators.id = products.cultivators_id WHERE products.id = %(id)s"
        result = connectToMySQL('weedproject').query_db(query, formulario) #Lista de diccionarios
        product = cls(result[0])
        return product

    @classmethod
    def terminar_compra(cls, formulario):
        query = "INSERT INTO shopping (name_bank, address, home_delivery, method_payment, state) VALUES (%(name_bank)s, %(address)s, %(home_delivery)s, %(method_payment)s, %(state)s);"
        result = connectToMySQL('weedproject').query_db(query, formulario)
        return result

    """@classmethod
    def update(cls, formulario):
        if(formulario['image'] != ''):
            query = "UPDATE crops SET farm=%(farm)s, state=%(state)s, municipality=%(municipality)s, fertilizer=%(fertilizer)s, f_amount=%(f_amount)s, date=%(date)s, disease=%(disease)s, production=%(production)s, description=%(description)s, image=%(image)s, share=%(share)s WHERE id = %(id)s"
        else:
            query = "UPDATE crops SET farm=%(farm)s, state=%(state)s, municipality=%(municipality)s, fertilizer=%(fertilizer)s, f_amount=%(f_amount)s, date=%(date)s, disease=%(disease)s, production=%(production)s, description=%(description)s, share=%(share)s WHERE id = %(id)s"
        result = connectToMySQL('weedproject').query_db(query, formulario)
        return result

    @classmethod
    def delete(cls, formulario):
        query = "DELETE FROM crops WHERE id = %(id)s;"
        result = connectToMySQL('weedproject').query_db(query, formulario)
        return result"""
