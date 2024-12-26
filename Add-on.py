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

######################## FUNCIÓN ADD-ON 1 ###############################
def move_obj_to_worldorigin():
    for obj in bpy.context.selected_objects:
        obj.select_set(False)
        obj.location = (0, 0, 0)
        obj.select_set(True)


######################## FUNCIÓN ADD-ON 2 ###############################
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


######################## FUNCIÓN ADD-ON 3 ###############################    
def create_background_torender():
    bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    bpy.ops.object.mode_set(mode = 'EDIT', toggle = False) 
    bpy.ops.mesh.select_mode(type="EDGE")

    me = bpy.context.edit_object.data

    bm = bmesh.from_edit_mesh(me)

    #EXTRUSIÓN
    for edge in bm.edges:
        edge.select = False
        
    for edge in bm.edges:
        if edge.index == 0:
            edge.select = True
            
    bpy.ops.mesh.extrude_edges_move(MESH_OT_extrude_edges_indiv={"use_normal_flip":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 2), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "use_duplicated_keyframes":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

    for edge in bm.edges:
        edge.select = False

    #REDONDEZ
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.shade_smooth()



            
    



######################## CLASE ADD-ON 1 ###############################
class MESH_OT_set_origin_in_selected(bpy.types.Operator):
    """Colocar el origen en el medio de las dos caras seleccionadas"""
    
    bl_idname = "mesh.set_origin_in_selected"  # Para que sea único y lo pueda llamar desde el panel
    bl_label = "En el centro de la seleccion"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        set_origin_in_selected()  # Llamar la función para mover al centro de las dos caras
        return {"FINISHED"}

######################## CLASE ADD-ON 2 ###############################
class MESH_OT_move_to_worldorigin(bpy.types.Operator):
    """Mover el origen de un objeto al del mundo"""
    
    bl_idname = "mesh.move_to_worldorigin"  # Para que sea único y lo pueda llamar desde el panel
    bl_label = "Al origen del mundo"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        move_obj_to_worldorigin()  # Llamar la función para mover al origen del mundo
        return {"FINISHED"}

######################## CLASE ADD-ON 3 ###############################    
class MESH_OT_create_background_torender(bpy.types.Operator):
    """Crear un fondo para renderizar"""
    
    bl_idname = "mesh.create_background_torender"  # Para que sea único y lo pueda llamar desde el panel
    bl_label = "Fondo para renderizar"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        create_background_torender()  # Llamar la función para crear el fondo
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
        row2.label(text="Mover el cursor 3D", icon = "WORLD_DATA")
        
        row2 = layout.row()
        row2.operator("mesh.set_origin_in_selected", icon="PROP_OFF")
        
        row3 = layout.row()
        row3.label(text="Crear", icon = "WORLD_DATA")
        
        row3 = layout.row()
        row3.operator("mesh.create_background_torender", icon="PROP_OFF")

# REGISTRAR LA CLASE

def register():
    bpy.utils.register_class(TestPanel)
    bpy.utils.register_class(MESH_OT_move_to_worldorigin)
    bpy.utils.register_class(MESH_OT_set_origin_in_selected)
    bpy.utils.register_class(MESH_OT_create_background_torender)


def unregister():
    bpy.utils.unregister_class(TestPanel)
    bpy.utils.unregister_class(MESH_OT_move_to_worldorigin)
    bpy.utils.unregister_class(MESH_OT_set_origin_in_selected)
    bpy.utils.unregister_class(MESH_OT_create_background_torender)

if __name__ == "__main__":
    register()