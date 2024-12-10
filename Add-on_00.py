bl_info = {
    "name" : "MyFisrtAddon",
    "description" : "Sample",
    "author" : "Carla",
    "version" : (0,0,1),
    "blender" : (4,2,3),
    
    "location" : "View3D > Sidebar > Herramientas Artista 3D",
    "category" : "Development",
}


import bpy

def move_obj_to_worldorigin:
    # Deseleccionar todo
    for i in bpy.context.selected_objects:
        object_name = i.name
        bpy.data.objects[object_name].select_set(False)


class MESH_OT_move_to_worldorigin( bpy.types.Operator ):
    """ Mover el origen de un objeto al del mundo """
    
    bl_idname = "mesh.move_to_worldorigin" # para que sea unico y lo pueda llamar desde el panel
    bl_label = "Mover el origen del objeto al origen del mundo"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        
        move_obj_to_worldorigin

        return { "FINISHED" }


class TestPanel( bpy.types.Panel ):
    bl_label = "Herramientas"   #Nombre
    bl_region_type = "UI"       # Zona de la pantalla
    bl_space_type = "VIEW_3D"   # Vista 3D
    bl_category = "Herramientas Artista 3D" # Nombre de la pestaña
    bl_idname = "3D_VIEW_PT_HerramientasArtista3D" # Prevenir duplicados
    
    def draw(self, context):
        layout = self.layout
        
        # Crea una fila nueva y me la devuelva
        row = layout.row()
        row.label(text = "Mover el origen del objeto", icon = "MESH_CUBE")
        
        row = layout.row()
        row.operator("mesh.add_sliced_cube", icon = "SNAP_VOLUME") # operator() es un bpy.ops


# REGISTRAR LA CLASE

def register():
    bpy.utils.register_class( TestPanel )
    bpy.utils.register_class( MESH_OT_add_sliced_cube )


def unregister():
    bpy.utils.unregister_class( TestPanel )
    bpy.utils.unregister_class( MESH_OT_add_sliced_cube )

if __name__ == "__main__":
    register()