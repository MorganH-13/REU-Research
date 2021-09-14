all: generate_graphene generate_Mn generate_combination move_file

generate_graphene:
	@echo "Making graphene cell..."
	@python3 GrapheneEditor.py

generate_Mn:
	@echo "Making Mn-12..."
	@python3 MnEditor.py

generate_combination:
	@echo "Combining system..."
	@python3 CombineMn_Graphene.py

move_file:
	@echo "Moving file..."
	@cp Comb.txt /Users/penguin/Desktop/REUResearch/Calculations/CombinedSystem/WVacancy/Orientation2/Height-6.45.txt
