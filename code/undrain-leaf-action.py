class evaluate_bgp_peers_status(Action):
    def run(self, bgp_state):
        if isinstance(bgp_state, dict):
            if len({p: pd for p, pd in bgp_state.items() 
                       if pd['local_as'] == pd['remote_as'] 
                       and pd["is_up"]}) < 1:
                return(False, "No underlay BGP established")
            else:
                return(True)
        else:
            return(False, "Expecting some json input")
