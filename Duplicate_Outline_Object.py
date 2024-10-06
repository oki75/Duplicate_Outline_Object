import bpy

bl_info = {
    "name": "Duplicate Outline Object",
    "blender": (3, 1, 0),
    "version": (1, 0),
    "author": "oki75",
    "description": "Outlineオブジェクトを作成",
    "category": "Object"
}


class OBJECT_OT_duplicate_Outline_Object(bpy.types.Operator):
    bl_idname = "object.duplicate_outline_object"
    bl_label = "Duplicate Outline Object"
    bl_description = "オブジェクトを複製し、アウトラインオブジェクトを作成します。"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # 複製元のオブジェクトをアクティブオブジェクトとして取得
        original_obj = context.active_object

        # オブジェクトが選択されているか確認
        if original_obj is None:
            self.report({'WARNING'}, "オブジェクトが選択されていません")
            return {'CANCELLED'}
        
        # オブジェクトを複製
        bpy.ops.object.duplicate_move()
        duplicated_obj = context.active_object
        
        # 複製オブジェクトの名前を元の名前 + "_Outline" に変更
        duplicated_obj.name = f"{original_obj.name}_Outline"

        # 頂点グループを追加
        vertex_group = duplicated_obj.vertex_groups.new(name="Group")

        # マテリアルを作成
        new_material = bpy.data.materials.new(f"{original_obj.name}_OutlineColor")
        new_material.diffuse_color = (0.1, 0.1, 0.1, 1)  # RGBAの形式で設定
        new_material.use_backface_culling = True

        # マテリアルをスロットに追加
        if len(duplicated_obj.material_slots) == 0:
            bpy.ops.object.material_slot_add()
        duplicated_obj.material_slots[0].material = new_material

        # Solidifyモディファイアを追加
        solidify_mod = duplicated_obj.modifiers.new(name="Solidify", type='SOLIDIFY')
        solidify_mod.use_flip_normals = True
        solidify_mod.offset = 0
        solidify_mod.material_offset = 1
        solidify_mod.thickness = 0.015
        solidify_mod.vertex_group = vertex_group.name

        # Surface Deform モディファイアを追加
        surface_deform_mod = duplicated_obj.modifiers.new(name="SurfaceDeform", type='SURFACE_DEFORM')
        surface_deform_mod.target = original_obj

        # Surface Deform をバインド（選択状態のオブジェクトに適用）
        bpy.context.view_layer.objects.active = duplicated_obj
        bpy.ops.object.surfacedeform_bind(modifier="SurfaceDeform")

        self.report({'INFO'}, f"{duplicated_obj.name} に Surface Deform モディファイアを追加し、ターゲットを {original_obj.name} に設定しました")

        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(OBJECT_OT_duplicate_Outline_Object.bl_idname)


def register():
    bpy.utils.register_class(OBJECT_OT_duplicate_Outline_Object)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_duplicate_Outline_Object)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()
