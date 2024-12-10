bl_info = {
    "name": "MyFirstAddon",
    "description": "Sample",
    "author": "Carla",
    "version": (0, 0, 1),
    "blender": (4, 2, 3),
    
    "location": "View3D > Sidebar > Herramientas Artista 3D",
    "category": "Development",
}


import bpy, bmesh

def move_obj_to_worldorigin():
    for obj in bpy.context.selected_objects:
        obj.select_set(False)
        obj.location = (0, 0, 0)
        obj.select_set(True)

def set_origin_in_selected():
    bpy.ops.object.mode_set(mode = 'EDIT', toggle = False) 
    bpy.ops.mesh.select_mode(type="VERT")

    me = bpy.context.edit_object.data
    
    bm = bmesh.from_edit_mesh(me)

    selected_edge = 0
    for index, vert in enumerate(bm.verts):
        if (vert.select == True) :
            selected_edge = index

    bm.verts[selected_edge]
    
    bpy.ops.view3d.snap_cursor_to_selected()
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')


class MESH_OT_set_origin_in_selected(bpy.types.Operator):
    """Colocar el origen en el medio de las dos caras seleccionadas"""
    
    bl_idname = "mesh.set_origin_in_selected"  # Para que sea único y lo pueda llamar desde el panel
    bl_label = "En el centro de la seleccion"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        set_origin_in_selected()  # Llamar la función para mover al origen del mundo
        return {"FINISHED"}

class MESH_OT_move_to_worldorigin(bpy.types.Operator):
    """Mover el origen de un objeto al del mundo"""
    
    bl_idname = "mesh.move_to_worldorigin"  # Para que sea único y lo pueda llamar desde el panel
    bl_label = "Al origen del mundo"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        move_obj_to_worldorigin()  # Llamar la función para mover al origen del mundo
        return {"FINISHED"}


class TestPanel(bpy.types.Panel):
    bl_label = "Herramientas"   # Nombre del panel
    bl_region_type = "UI"       # Zona de la pantalla
    bl_space_type = "VIEW_3D"   # Vista 3D
    bl_category = "Herramientas Artista 3D" # Nombre de la pestaña
    bl_idname = "3D_VIEW_PT_HerramientasArtista3D" # Prevenir duplicados
    
    def draw(self, context):
        layout = self.layout
        
        # Crear una fila nueva
        row = layout.row()
        row.label(text="Mover el objeto", icon="UNPINNED")
        
        # Botón para ejecutar el operador
        row = layout.row()
        row.operator("mesh.move_to_worldorigin", icon="TRACKER")  # Referencia al operador creado

        row2 = layout.row()
        row2.label(text="Mover el origen", icon = "WORLD_DATA")
        
        row2 = layout.row()
        row2.operator("mesh.set_origin_in_selected", icon="PROP_OFF")

# REGISTRAR LA CLASE

def register():
    bpy.utils.register_class(TestPanel)
    bpy.utils.register_class(MESH_OT_move_to_worldorigin)
    bpy.utils.register_class(MESH_OT_set_origin_in_selected)


def unregister():
    bpy.utils.unregister_class(TestPanel)
    bpy.utils.unregister_class(MESH_OT_move_to_worldorigin)
    bpy.utils.unregister_class(MESH_OT_set_origin_in_selected)

if __name__ == "__main__":
    register()
