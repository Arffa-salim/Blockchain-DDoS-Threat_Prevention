// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DDoSDecisionLog {

    struct Decision {
        string ip;
        uint requestCount;
        string finalDecision;
        uint timestamp;
    }

    Decision[] public decisions;

    function addDecision(
        string memory _ip,
        uint _requestCount,
        string memory _finalDecision
    ) public {

        decisions.push(
            Decision(
                _ip,
                _requestCount,
                _finalDecision,
                block.timestamp
            )
        );
    }

    function getDecision(uint index)
        public
        view
        returns (
            string memory,
            uint,
            string memory,
            uint
        )
    {
        Decision memory d = decisions[index];

        return (
            d.ip,
            d.requestCount,
            d.finalDecision,
            d.timestamp
        );
    }

    function getTotalDecisions()
        public
        view
        returns (uint)
    {
        return decisions.length;
    }
}
