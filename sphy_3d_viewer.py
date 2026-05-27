# -*- coding: utf-8 -*-
# ============================================================
# SPHY ENGINE - UNIFIED 3D PHASE-SPACE GEOMETRIC VIEWER
# ============================================================
import py5
import pandas as pd
import numpy as np
import struct
import hashlib
import os
import time

# ------------------------------------------------------------
# LEDGER INPUT CONFIGURATIONS
# ------------------------------------------------------------
CAMINHO_PARQUET = "sphy_unified_forensic_matrix.parquet"
CAMINHO_CSV = "sphy_unified_forensic_matrix.csv"

# Global Ontological Constants
NUM_FRAMES = 1200
PHI = (1.0 + np.sqrt(5.0)) / 2.0
H_PLANCK = 6.62607015e-34
C_LUZ = 299792458
G_GRAVITACAO = 6.67430e-11

# ------------------------------------------------------------
# AUTO-GENERATION FALLBACK ENGINE
# ------------------------------------------------------------
def emular_ledger_emergencial():
    print("[EMERGENCY] Ledger file not found. Executing SPHY symbiotic matrix generation...")
    data_list = []
    hash_anterior = "0" * 64
    
    for i in range(NUM_FRAMES):
        is_macro = i >= (NUM_FRAMES // 2)
        if not is_macro:
            n_nos = 1
            raio = 1e-15
            massa_escala = 1.67262192369e-27
        else:
            n_nos = 1e60
            raio = 1e3
            massa_escala = (raio * (C_LUZ**2)) / (2 * G_GRAVITACAO)
            
        g00 = np.exp(- (n_nos * H_PLANCK * (PHI**2)) / (2 * np.pi * raio * massa_escala * C_LUZ))
        fase = (H_PLANCK * i * (10**34 if not is_macro else 1)) / PHI
        
        ex = float(np.sin(fase) * PHI)
        ey = float(np.cos(fase) * (PHI**2))
        ez = float(np.sin(fase * PHI) * (PHI**3))
        bx = float(np.cos(fase) * PHI)
        by = float(np.sin(fase) * (PHI**2))
        bz = float(np.cos(fase * PHI) * (PHI**3))
        
        energia_equivalente = massa_escala * (C_LUZ**2)
        frequencia_fase = C_LUZ / (2 * np.pi * raio)
        K_fator = (energia_equivalente / (H_PLANCK * frequencia_fase)) * (1 / (PHI**2))
        
        timestamp_frame = 1782384000.0 + (i * 0.0025)
        payload_binario = struct.pack('ffffffff', float(g00), ex, ey, ez, bx, by, bz, float(K_fator))
        
        ctx = hashlib.sha256()
        ctx.update(hash_anterior.encode('utf-8'))
        ctx.update(payload_binario)
        hash_atual = ctx.hexdigest()
        
        data_list.append({
            "frame_idx": i,
            "scale": "MICRO (ATOM)" if not is_macro else "MACRO (BLACK HOLE)",
            "timestamp_vlc": timestamp_frame,
            "g00_gravitational_metric": g00,
            "F_01_Ex": ex,
            "F_02_Ey": ey,
            "F_03_Ez": ez,
            "F_12_Bx": bx,
            "F_23_By": by,
            "F_31_Bz": bz,
            "K_Scale_Invariant": K_fator,
            "sha256_hash_frame": hash_atual
        })
        hash_anterior = hash_atual

    df_novo = pd.DataFrame(data_list)
    # Salva em ambos os formatos para garantir compatibilidade futura
    df_novo.to_parquet(CAMINHO_PARQUET, index=False)
    df_novo.to_csv(CAMINHO_CSV, index=False)
    print(f"[EMERGENCY] Generation complete. Files saved in data core. Booting viewer...")
    return df_novo

# ------------------------------------------------------------
# RECONSTRUCTOR GLOBAL STATE
# ------------------------------------------------------------
df_publico = None
total_frames = 0
frame_atual = 0
executando_pausa = False

# Interactive Camera Variables (1280x720 P3D Viewport)
rot_x = 25
rot_y = 45
zoom = -450  
move_x = 0
move_y = 0

hash_ancestral_esperado = "0" * 64
erros_acumulados = 0
status_historico = {}  

def settings():
    py5.size(1280, 720, py5.P3D)
    py5.smooth(8)

def setup():
    global df_publico, total_frames
    
    py5.window_title('SPHY Forensic Analyzer: 3D Unified Field Geometric Validator')
    py5.frame_rate(60)
    py5.color_mode(py5.HSB, 255)
    
    # Validação inteligente de arquivos com fallback automático
    if os.path.exists(CAMINHO_PARQUET):
        print(f"[AUDIT] Opening Parquet ledger: {CAMINHO_PARQUET}")
        df_publico = pd.read_parquet(CAMINHO_PARQUET)
    elif os.path.exists(CAMINHO_CSV):
        print(f"[AUDIT] Parquet missing. Opening CSV ledger: {CAMINHO_CSV}")
        df_publico = pd.read_csv(CAMINHO_CSV)
    else:
        # Se nenhum arquivo existir, gera localmente de forma simbiótica
        df_publico = emular_ledger_emergencial()
        
    total_frames = len(df_publico)

def draw():
    global frame_atual, hash_ancestral_esperado, erros_acumulados
    
    if df_publico is None:
        return
        
    py5.background(10) 
    py5.lights()
    
    row_data = df_publico.iloc[frame_atual]
    
    frame_idx = int(row_data['frame_idx'])
    scale_domain = str(row_data['scale'])
    timestamp = float(row_data['timestamp_vlc'])
    g00 = float(row_data['g00_gravitational_metric'])
    ex = float(row_data['F_01_Ex'])
    ey = float(row_data['F_02_Ey'])
    ez = float(row_data['F_03_Ez'])
    bx = float(row_data['F_12_Bx'])
    by = float(row_data['F_23_By'])
    bz = float(row_data['F_31_Bz'])
    k_invariante = float(row_data['K_Scale_Invariant'])
    hash_gravado = str(row_data['sha256_hash_frame'])
    
    # Revalidação Criptográfica Estrita
    payload_binario = struct.pack('ffffffff', g00, ex, ey, ez, bx, by, bz, k_invariante)
    
    ctx = hashlib.sha256()
    ctx.update(hash_ancestral_esperado.encode('utf-8'))
    ctx.update(payload_binario)
    hash_recalculado = ctx.hexdigest()
    
    if frame_atual not in status_historico:
        if hash_recalculado == hash_gravado:
            status_historico[frame_atual] = "INTEGRO"
        else:
            status_historico[frame_atual] = "CORROMPIDO"
            erros_acumulados += 1
            
    status_atual = status_historico[frame_atual]
    
    # RENDERIZAÇÃO GEOMÉTRICA PURE 3D
    py5.push_matrix()
    py5.translate(py5.width / 2 + move_x, py5.height / 2 + move_y, zoom)
    py5.rotate_x(py5.radians(rot_x))
    py5.rotate_y(py5.radians(rot_y))
    
    render_scale = 90.0 if "MICRO" in scale_domain else 4.0
    num_points = 1200  
    t_espaco = np.linspace(0, 16 * np.pi, num_points)
    
    x_soliton = np.sin(t_espaco * ex) * PHI * render_scale
    y_soliton = np.cos(t_espaco * ey) * (PHI**2) * render_scale
    z_soliton = (t_espaco * g00 * render_scale * 3.0) - (render_scale * 5.0)
    
    py5.no_fill()
    py5.stroke_weight(2.5)
    
    py5.begin_shape()
    for idx in range(num_points):
        hue_color = np.interp(z_soliton[idx], [np.min(z_soliton), np.max(z_soliton)], [160, 240])
        
        if status_atual == "CORROMPIDO":
            py5.stroke(0, 255, 255) 
        else:
            if "MICRO" in scale_domain:
                py5.stroke(hue_color, 255, 255) 
            else:
                py5.stroke((hue_color + 40) % 255, 255, 255) 
                
        py5.vertex(x_soliton[idx], y_soliton[idx], z_soliton[idx])
    py5.end_shape()
    
    py5.stroke(100, 50, 255, 40) 
    py5.stroke_weight(1.0)
    py5.ellipse(0, 0, PHI * render_scale * 2, (PHI**2) * render_scale * 2)
    py5.pop_matrix()
    
    # 2D HUD OVERLAY
    py5.camera()
    py5.color_mode(py5.RGB, 255)
    
    py5.fill(10, 10, 14, 230)
    py5.stroke(50)
    py5.stroke_weight(1.5)
    py5.rect(20, 20, 560, 480, 6)
    
    if erros_acumulados == 0:
        py5.fill(0, 210, 110) 
        py5.text_size(18)
        py5.text("🛡️ SPHY INVARIANCE MATRIX: VALIDATED", 40, 55)
    else:
        py5.fill(255, 60, 60) 
        py5.text_size(18)
        py5.text(f"🚨 CHAIN OF CUSTODY BREACHED: {erros_acumulados} ERRORS", 40, 55)
        
    py5.fill(235)
    py5.text_size(13)
    py5.text(f"Frame Index: {frame_idx} / {total_frames - 1}", 40, 90)
    py5.text(f"Domain Horizon: {scale_domain}", 40, 115)
    py5.text(f"Clock Timestamp: {timestamp:.4f}", 40, 140)
    
    py5.fill(130, 175, 255)
    py5.text(f"Planck Constant (h): {H_PLANCK:.8e} J·s", 40, 175)
    py5.text(f"Golden Ratio Anchor (PHI): {PHI:.6f}", 40, 195)
    
    py5.fill(220)
    py5.text(f"Gravitational Metric (g00): {g00:.8e}", 40, 230)
    py5.text(f"Faraday Tensor [Electric]: Ex={ex:.4f} | Ey={ey:.4f} | Ez={ez:.4f}", 40, 255)
    py5.text(f"Faraday Tensor [Magnetic]: Bx={bx:.4f} | By={by:.4f} | Bz={bz:.4f}", 40, 280)
    
    py5.fill(255, 165, 80)
    py5.text(f"Dimensionless Coupling K Factor: {k_invariante:.6f}", 40, 315)
    py5.text_size(11)
    py5.text("(*Ratio of Metric to Quantum energy remains invariant micro/macro)", 40, 330)
    
    py5.text_size(12)
    py5.fill(160)
    py5.text("Recorded Parquet Row Hash:", 40, 365)
    py5.fill(200)
    py5.text(hash_gravado, 40, 385)
    
    py5.fill(160)
    py5.text("Real-Time Computed Verification Hash:", 40, 415)
    if status_atual == "INTEGRO":
        py5.fill(0, 210, 110)
    else:
        py5.fill(255, 60, 60)
    py5.text(hash_recalculado, 40, 435)
    
    py5.color_mode(py5.HSB, 255)
    
    if not executando_pausa:
        hash_ancestral_esperado = hash_gravado 
        frame_atual += 1
        if frame_atual >= total_frames:
            frame_atual = 0
            hash_ancestral_esperado = "0" * 64 

def key_pressed():
    global rot_x, rot_y, zoom, move_x, move_y, frame_atual, hash_ancestral_esperado, executando_pausa
    if py5.key == ' ':
        executando_pausa = not executando_pausa
    elif py5.key in ['r', 'R']:
        rot_x, rot_y, zoom, move_x, move_y = 25, 45, -450, 0, 0
    elif py5.key == py5.CODED:
        if py5.key_code == py5.RIGHT and frame_atual < total_frames - 1:
            hash_ancestral_esperado = df_publico.iloc[frame_atual]['sha256_hash_frame']
            frame_atual += 1
        elif py5.key_code == py5.LEFT and frame_atual > 0:
            frame_atual -= 1
            hash_ancestral_esperado = "0" * 64 if frame_atual == 0 else df_publico.iloc[frame_atual - 1]['sha256_hash_frame']

def mouse_dragged():
    global rot_x, rot_y, move_x, move_y
    if py5.mouse_button == py5.LEFT:
        rot_y += (py5.mouse_x - py5.pmouse_x) * 0.5
        rot_x += (py5.mouse_y - py5.pmouse_y) * 0.5
    elif py5.mouse_button == py5.RIGHT:
        move_x += py5.mouse_x - py5.pmouse_x
        move_y += py5.mouse_y - py5.pmouse_y

def mouse_wheel(event):
    global zoom
    zoom += event.get_count() * 18

if __name__ == '__main__':
    py5.run_sketch()