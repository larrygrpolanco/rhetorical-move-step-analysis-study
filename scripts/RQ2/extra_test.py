from scipy.stats import fligner, mannwhitneyu

# Load your data
zero_shot_move = df_zero_shot["move_accuracy"].values
finetuned_move = df_finetuned["move_accuracy"].values
zero_shot_step = df_zero_shot["step_accuracy"].values
finetuned_step = df_finetuned["step_accuracy"].values

# Fligner-Killeen (variance comparison)
fk_move_stat, fk_move_p = fligner(zero_shot_move, finetuned_move)
fk_step_stat, fk_step_p = fligner(zero_shot_step, finetuned_step)

print(f"Fligner-Killeen (Move): χ²={fk_move_stat:.2f}, p={fk_move_p:.4f}")
print(f"Fligner-Killeen (Step): χ²={fk_step_stat:.2f}, p={fk_step_p:.4f}")

# Mann-Whitney U (mean comparison)
mw_move_stat, mw_move_p = mannwhitneyu(
    zero_shot_move, finetuned_move, alternative="two-sided"
)
mw_step_stat, mw_step_p = mannwhitneyu(
    zero_shot_step, finetuned_step, alternative="two-sided"
)

print(f"Mann-Whitney U (Move): U={mw_move_stat:.0f}, p={mw_move_p:.4f}")
print(f"Mann-Whitney U (Step): U={mw_step_stat:.0f}, p={mw_step_p:.4f}")
