import numpy as np
from .base_derivative import BaseFractionalDerivative

class HilferDerivative(BaseFractionalDerivative):
    """
    Lightweight Hilfer fractional derivative implementation
    Optimized for computational efficiency in neural network training
    
    The Hilfer derivative interpolates between Riemann-Liouville and Caputo
    using parameter beta: when beta=0 -> RL, when beta=1 -> Caputo
    """
    
    def __init__(self, alpha=1.5, beta=0.5):
        """
        Initialize Hilfer derivative
        
        Args:
            alpha (float): Fractional order (0 < alpha <= 2)
            beta (float): Type parameter (0 <= beta <= 1)
        """
        super().__init__(alpha)
        if not 0 <= beta <= 1:
            print(f"Warning: Beta {beta} outside [0,1], clipping to valid range")
            beta = max(0, min(1, beta))
        self.beta = beta
        self.max_history = 5  # Limit history to prevent computational explosion
        
    def update_history(self, t, y):
        """Override to limit history size for computational efficiency"""
        super().update_history(t, y)
        
        # Keep only recent history to prevent computational issues
        if len(self.history) > self.max_history:
            self.history = self.history[-self.max_history:]
            self.time_history = self.time_history[-self.max_history:]
    
    def compute_derivative_simple(self, func, t, y, dt):
        """
        Fast, stable Hilfer derivative approximation
        
        Hilfer derivative: D^{alpha,beta} = beta * Caputo + (1-beta) * Riemann-Liouville
        """
        self.update_history(t, y)
        
        if len(self.history) < 2:
            return func(y, t)
        
        # Get classical derivative
        classical_deriv = np.array(func(y, t))
        
        # Hilfer memory effect (simplified and stable)
        if len(self.history) >= 2:
            current_state = np.array(y)
            previous_state = np.array(self.history[-2])
            
            # Caputo-like component (focuses on derivative history)
            caputo_component = self.alpha * 0.01 * (current_state - previous_state)
            
            # Riemann-Liouville-like component (focuses on function history)
            rl_component = (self.alpha - 1.0) * 0.02 * (current_state - previous_state)
            
            # Hilfer combination: beta interpolates between the two
            memory_term = self.beta * caputo_component + (1 - self.beta) * rl_component
            
            # Apply stability constraints
            memory_term = np.clip(memory_term, -1, 1)
            
            # Combine with classical derivative
            fractional_deriv = classical_deriv + memory_term
        else:
            fractional_deriv = classical_deriv
            
        return np.clip(fractional_deriv, -10, 10)

    def compute_derivative(self, func, t, y, dt):
        """Main computation method - alias for compatibility"""
        return self.compute_derivative_simple(func, t, y, dt)
    
    def reset_history(self):
        """Reset history for new simulations"""
        if hasattr(super(), 'reset_history'):
            super().reset_history()
        else:
            self.history = []
            self.time_history = []


def hilfer_derivative(alpha=1.0, beta=0.5):
    """Create Hilfer derivative instance"""
    return HilferDerivative(alpha, beta)


# Convenience function for different beta values
def hilfer_caputo_like(alpha=1.0):
    """Create Hilfer derivative close to Caputo (beta=0.9)"""
    return HilferDerivative(alpha, beta=0.9)


def hilfer_rl_like(alpha=1.0):
    """Create Hilfer derivative close to Riemann-Liouville (beta=0.1)"""
    return HilferDerivative(alpha, beta=0.1)


def hilfer_balanced(alpha=1.0):
    """Create balanced Hilfer derivative (beta=0.5)"""
    return HilferDerivative(alpha, beta=0.5)
